"""Python SDK for DERO Merchant REST API

This module allows developers to interact with the DERO Merchant REST API.

Requires:
    requests (module)

Exports:
    Client (class): exposes methods to send requests to the API.
    APIError (Exception): representation of the error object returned by the API.
    verify_webhook_signature (function): verifies the signature of requests to the webhook.
"""

from .client import Client
from .api_error import APIError
from .webhook import verify_webhook_signature
