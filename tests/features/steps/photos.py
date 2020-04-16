# type: ignore
import os

import httpx
from behave import given, then, when

ZATO_HOST = os.getenv("ZATO_HOST", "http://zato:11223")
SERVICE_ENDPOINT = f"{ZATO_HOST}/photos/get-photo/"


@when("I try to see a photo {photo_id}")
def step_get_photo(context, photo_id):
    headers = {}
    if hasattr(context, "headers"):
        headers = context.headers
    context.response = httpx.get(
        f"{SERVICE_ENDPOINT}{photo_id}/", headers=headers
    )
