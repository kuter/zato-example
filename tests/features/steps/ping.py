# type: ignore
import os

import requests
from behave import given, then, when


ZATO_HOST = os.getenv("ZATO_HOST", "http://zato:11223")


@given(u'built-in ping service')
def step_given(context):
    pass


@when(u'we call ping service')
def step_call_ping(context):
    context.response = requests.get(f"{ZATO_HOST}/zato/ping")


@then(u'response should be ok')
def step_response_ok(context):
    assert context.response.ok is True
