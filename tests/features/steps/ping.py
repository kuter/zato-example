# type: ignore
import os

import httpx
from behave import given, then, when


ZATO_HOST = os.getenv("ZATO_HOST", "http://zato:11223")
SERVICE_ENDPOINT = f"{ZATO_HOST}/zato/ping"


@given("built-in ping service")
def step_given(context):
    pass


@when("we call ping service")
def step_call_ping(context):
    context.response = httpx.get(SERVICE_ENDPOINT)


@then("response should be ok")
def step_response_ok(context):
    assert context.response.status_code == 200
