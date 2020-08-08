import requests
import json
from .crypto_util import sign_message
from .api_error import APIError

DEFAULT_SCHEME = "https"
DEFAULT_HOST = "merchant.dero.io"
DEFAULT_API_VERSION = "v1"

class Client:
    """Dero Merchant Client. Has methods to interact with the Dero Merchant REST API.

    Attributes:
        __scheme: String of the scheme of the URL of the API.
        __host: String of the host of the URL of the API.
        __api_version: String of the version of the API.
        __base_url: URL of the API.
        timeout: Integer of the seconds before a connection to the API times out.
        __api_key: String of the API Key of the Client.
        __secret_key: String of the Secret Key of the Client.
    """
 
    def __init__(self, api_key: str, secret_key: str, scheme=DEFAULT_SCHEME, host=DEFAULT_HOST, api_version=DEFAULT_API_VERSION):
        """Inits Client with API Key, Secret Key, scheme, host and API Version

        Args:
            api_key: String of the API Key of the Client.
            secret_key: String of the Secret Key of the Client.
            scheme: String of the scheme of the URL of the API.
            host: String of the host of the URL of the API.
            api_version: String of the version of the API.
        """

        self.__scheme = scheme
        self.__host = host
        self.__api_version = api_version
        self.__base_url = f'{self.__scheme}://{self.__host}/api/{self.__api_version}'
        self.timeout = 10

        self.__api_key = api_key
        self.__secret_key = secret_key
    
    def __send_request(self, method: str, endpoint: str, query_params: dict=None, payload=None, sign_body=False) -> dict:
        """Sends a request to the API.
        
        Args:
            method: String of the method of the request.
            endpoint: String of the endpoint of the request.
            query_params: Dictionary of the query params to send in the request.
            payload: Payload to send as the JSON body of the request.
            sign_body: Bool of whether the request body has to be signed or not.

        Returns:
            A dictionary of the JSON response.

        Raises:
            Exception: An error occured send the request.
            APIError: An error was returned as a response by the API.
        """
        url = self.__base_url + endpoint
        headers = {
            "User-Agent": "DeroMerchant_Client_Python/1.0",
            "X-API-Key": self.__api_key,
        }

        json_payload = None
        json_res = None

        try:
            if payload is not None:
                headers["Content-Type"] = "application/json"
                headers["Accept"] = "applciation/json"

                json_payload = json.dumps(payload, separators=(",", ":"))

                if sign_body is not False:
                    signature = sign_message(json_payload, self.__secret_key)
                    headers["X-Signature"] = signature

            res = requests.request(method, url, timeout=self.timeout, params=query_params, headers=headers, data=json_payload)
            if "application/json" in res.headers.get("Content-Type"):
                json_res = res.json()

            if (res.status_code < 200) or (res.status_code > 299):
                if (json_res is not None) and ("error" in json_res):
                    raise APIError(json_res["error"]["code"], json_res["error"]["message"])
                else:
                    if res.status_code == 404:
                        raise Exception(f'error 404: page {res.url} not found')
                    else:
                        raise Exception(f'error {res.status_code} returned by {res.url}')
        except Exception as err:
            raise Exception(f'DeroMerchant Client: {err}')
        else:
            return json_res

    def ping(self) -> dict:
        """Pings the API.

        Returns:
            A dictionary with the JSON response.
        """
        return self.__send_request(
            method="GET",
            endpoint="/ping"
        )

    def create_payment(self, currency: str, amount: float) -> dict:
        """Creates a new payment.

        Args:
            currency: String of the currency of the payment.
            amount: Float of the amount of the payment.

        Returns:
            A dictionary with the JSON response of the newly created Payment.
        """
        return self.__send_request(
            method="POST",
            endpoint="/payment",
            payload={
                "currency": currency,
                "amount": amount,
            },
            sign_body=True
        )

    def get_payment(self, payment_id: str) -> dict:
        """Gets a payment from its ID.

        Args:
            payment_id: String of the payment ID.

        Returns:
            A dictionary with the JSON response of the requested Payment.
        """
        return self.__send_request(
            method="GET",
            endpoint=f'/payment/{payment_id}'
        )

    def get_payments(self, payment_ids: list) -> list:
        """Gets payments from their IDs.

        Args:
            payment_ids: List of strings of the payment IDs.
        
        Returns:
            A list containing dictionaries with the JSON response of the requested payments. 
        """
        return self.__send_request(
            method="POST",
            endpoint="/payments",
            payload=payment_ids
        )

    def get_filtered_payments(self, limit: int=None, page: int=None, sort_by: str=None, order_by: str=None, filter_status:str=None, filter_currency: str=None) -> dict:
        """Gets filtered payments"""
        return self.__send_request(
            method="GET",
            endpoint="/payments",
            query_params={
                "limit": limit,
                "page": page,
                "sort_by": sort_by,
                "order_by": order_by,
                "filter_status": filter_status,
                "filter_currency": filter_currency,
            }
        )

    def get_pay_helper_url(self, payment_id: str) -> str:
        """Gets the URL of the Pay helper page of the payment ID.

        Args:
            payment_id: String of the payment ID.

        Returns:
            String with the URL of the Pay helper page of the payment ID.
        """
        return f'{self.__scheme}://{self.__host}/pay/{payment_id}'
