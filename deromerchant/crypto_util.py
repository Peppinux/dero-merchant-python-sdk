import hmac
import hashlib
import binascii

def sign_message(message: str, key: str) -> str:
    """Signs a message with a key.

    Args:
        message:
            String of the message we want to sign.
        key:
            String of the SHA256 hex encoded key we want to use to sign the message.
    
    Returns:
        A string containing the SHA256 hex encoded signature of the message.
    """

    key_bytes = binascii.unhexlify(key)
    message_bytes = message.encode()
    return hmac.new(key_bytes, message_bytes, hashlib.sha256).hexdigest()

def valid_mac(message: str, message_mac: str, key: str) -> bool:
    """Verifies if the signature of a message is valid.

    Args:
        message:
            String of the message we want to verify.
        message_mac:
            String of the SHA256 hex encoded signature of the message we want to verify.
        key:
            String of the SHA256 hex encoded key used to sign the message.

    Returns:
        A bool with the validity of the signature.
    """
    signed_message = sign_message(message, key)
    return hmac.compare_digest(bytearray.fromhex(message_mac), bytearray.fromhex(signed_message))
