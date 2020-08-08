# DERO Merchant Python SDK
Library with bindings for the [DERO Merchant REST API](https://merchant.dero.io/docs) for accepting DERO payments on a Python backend.

## Requirements
- A store registered on your [DERO Merchant Dashboard](https://merchant.dero.io/dashboard) to receive an API Key and a Secret Key, required to send requests to the API.
- A Python web server.

## Installation
`pip install dero-merchant-python-sdk`

## Usage
### Import
`import deromerchant`

### Setup
```python
dm_client = deromerchant.Client(
    "API_KEY_OF_YOUR_STORE_GOES_HERE", # REQUIRED
    "SECRET_KEY_OF_YOUR_STORE_GOES_HERE", # REQUIRED
    scheme="https", # OPTIONAL. Default: https
    host="merchant.dero.io", # OPTIONAL. Default: merchant.dero.io
    api_version="v1", # OPTIONAL. Default: v1
)

try:
    res = dm_client.ping()
    print(res) # {"ping":"pong"}
except deromerchant.APIError as api_err:
    # Error returned by the API. Probably invalid API Key.
    print(api_err)
except Exception as err:
    # Somethign went wrong while sending the request.
    # The server is offline or bad scheme/host/api version were provided.
    print(err)
```

### Create a Payment
```python
try:
    # payment = dm_client.create_payment("USD", 1) // USD value will be converted to DERO
    # payment = dm_client.create_payment("EUR", 100) // Same thing goes for EUR and other currencies supported by the CoinGecko API V3
    payment = dm_client.create_payment("DERO", 10)

    print(payment)
    """
        Dictionary
        {
            'paymentID': '9ad7fd4ccd85035b30bb8f3f4bea058d50fb38c6b12aca83bedc2bbc21a3d1b1',
            'status': 'pending',
            'currency': 'DERO',
            'currencyAmount': 10,
            'exchangeRate': 1,
            'deroAmount': '10.000000000000',
            'atomicDeroAmount': 10000000000000,
            'integratedAddress': 'dETin8HwLs94N6j8zASZjD8htBbQTkhUuicZEYKBG6zQENd8mrhopv3YqaeP3Q9q1RMLHX3PvF4F4Xy1cN3Rndq7daiU3kG58ZaPFPqhm3i2KCg9Jc2nRSb3n8A8NFpz9mWp7D4kJcC2dY',
            'creationTime': '2020-08-02T22:14:56.119235Z',
            'ttl': 60
        }
    """
except deromerchant.APIError as api_err:
    # Handle API Error
except Exception as err:
    # Handle error
```

### Get a Payment from its ID
```python
try:
    payment_id = "9ad7fd4ccd85035b30bb8f3f4bea058d50fb38c6b12aca83bedc2bbc21a3d1b1"
    payment = dm_client.get_payment(payment_id)

    print(payment)
    """
        Dictionary
        {
            'paymentID': '9ad7fd4ccd85035b30bb8f3f4bea058d50fb38c6b12aca83bedc2bbc21a3d1b1',
            'status': 'pending',
            'currency': 'DERO',
            'currencyAmount': 10,
            'exchangeRate': 1,
            'deroAmount': '10.000000000000',
            'atomicDeroAmount': 10000000000000,
            'integratedAddress': 'dETin8HwLs94N6j8zASZjD8htBbQTkhUuicZEYKBG6zQENd8mrhopv3YqaeP3Q9q1RMLHX3PvF4F4Xy1cN3Rndq7daiU3kG58ZaPFPqhm3i2KCg9Jc2nRSb3n8A8NFpz9mWp7D4kJcC2dY',
            'creationTime': '2020-08-02T22:14:56.119235Z',
            'ttl': 55
        }
    """
except deromerchant.APIError as api_err:
    # Handle API Error
except Exception as err:
    # Handle error
```

### Get an array of Payments from their IDs
```python
try:
    payment_ids = ["9ad7fd4ccd85035b30bb8f3f4bea058d50fb38c6b12aca83bedc2bbc21a3d1b1", "7d3dadd862344b2792a591d92391e49fdb15c3b0db6fe73b901000c54c97922c"]
    payments = dm_client.get_payments(payment_ids)

    print(payments)
    """
        List of dictionaries
        [
            {
                'paymentID': '7d3dadd862344b2792a591d92391e49fdb15c3b0db6fe73b901000c54c97922c',
                'status': 'error',
                'currency': 'USD',
                'currencyAmount': 10,
                'exchangeRate': 1.18,
                'deroAmount': '8.474576271186',
                'atomicDeroAmount': 8474576271186,
                'integratedAddress': 'dETin8HwLs94N6j8zASZjD8htBbQTkhUuicZEYKBG6zQENd8mrhopv3YqaeP3Q9q1RMLHX3PvF4F4Xy1cN3Rndq7daiTzQYtH859kKAUCwhfgvRQM3BVMsaEvKibuCxfRoMD6k9MK7wtBk',
                'creationTime': '2020-08-02T14:59:54.259882Z',
                'ttl': 0
            },
            {
                'paymentID': '9ad7fd4ccd85035b30bb8f3f4bea058d50fb38c6b12aca83bedc2bbc21a3d1b1',
                'status': 'pending',
                'currency': 'DERO',
                'currencyAmount': 10,
                'exchangeRate': 1,
                'deroAmount': '10.000000000000',
                'atomicDeroAmount': 10000000000000,
                'integratedAddress': 'dETin8HwLs94N6j8zASZjD8htBbQTkhUuicZEYKBG6zQENd8mrhopv3YqaeP3Q9q1RMLHX3PvF4F4Xy1cN3Rndq7daiU3kG58ZaPFPqhm3i2KCg9Jc2nRSb3n8A8NFpz9mWp7D4kJcC2dY',
                'creationTime': '2020-08-02T22:14:56.119235Z',
                'ttl': 52
            }
        ]
    """
except deromerchant.APIError as api_err:
    # Handle API Error
except Exception as err:
    # Handle error
```

### Get an array of filtered Payments
_Not detailed because this endpoint was created for an internal usecase._
```python
try:
    res = dm_client.get_filtered_payments(
        limit=None,
        page=None,
        sort_by=None,
        order_by=None,
        filter_status=None,
        filter_currency=None
    )

    print(res) # Dictionary
except deromerchant.APIError as api_err:
    # Handle API Error
except Exception as err:
    # Handle error
```

### Get Pay helper page URL
```python
payment_id = "9ad7fd4ccd85035b30bb8f3f4bea058d50fb38c6b12aca83bedc2bbc21a3d1b1"
pay_url = dm_client.get_pay_helper_url(payment_id)

print(pay_url) # https://merchant.dero.io/pay/9ad7fd4ccd85035b30bb8f3f4bea058d50fb38c6b12aca83bedc2bbc21a3d1b1
```

### Verify Webhook Signature
When using Webhooks to receive Payment status updates, it is highly suggested to verify the HTTP requests are actually sent by the DERO Merchant server thorugh the X-Signature header.

**Example using Flask**
```python
import deromerchant
import json
from flask import Flask, request
app = Flask(__name__)

WEBHOOK_SECRET_KEY = "WEBHOOK_SECRET_KEY_OF_YOUR_STORE_GOES_HERE"

@app.route("/dero_merchant_webhook_example", methods=["POST"])
def hello_world():
    try:
        req_json = request.get_json() # Dictionary
        req_body = json.dumps(req_json, separators=(",", ":")) # String, required by verify_webhook_signature
        req_signature = request.headers["X-Signature"]
        valid = deromerchant.verify_webhook_signature(req_body, req_signature, WEBHOOK_SECRET_KEY)

        if valid:
            # Signature was verified. As such, as long Webhook Secret Key was stored securely, request should be trusted.
            # Proceed with updating the status of the order on your store associated to req_json["paymentID"] accordingly to req_json["status"]
            
            print(req_json)
            """
                Dictionary
                {
                    'status': 'paid',
                    'paymentID': '38ad8cf0c5da388fe9b5b44f6641619659c99df6cdece60c6e202acd78e895b1'
                }
            """
        else:
            # Signature of the body provided in the request does not match the signature of the body generated using webhook_secret_key.
            # As such, REQUEST SHOULD NOT BE TRUSTED.
            # This could also mean a wrong WEBHOOK_SECRET_KEY was provided as a param, so be extra careful when copying the value from the Dashboard.
    except Exception as err:
        # Handle error
    return ("", 204) # No response needed
```
