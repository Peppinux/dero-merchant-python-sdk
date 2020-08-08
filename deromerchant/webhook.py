from .crypto_util import valid_mac

def verify_webhook_signature(req_body: str, req_signature: str, webhook_secret_key: str) -> bool:
    """Verifies the signature of a webhook request.

    Args:
        req_body:
            A string of the body of the webhook request.
        req_signature:
            A string of the SHA256 hex encoded signature of the body of the webhook request.
        webhook_secret_key:
            A string of the SHA256 hex encoded webhook secret key.
    Returns:
        A bool with the validity of the signature.
    """
    return valid_mac(req_body, req_signature, webhook_secret_key)
