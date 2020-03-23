# type: ignore
import os

import httpx
from behave import given, then, when

ZATO_HOST = os.getenv("ZATO_HOST", "http://zato:11223")
SERVICE_ENDPOINT = f"{ZATO_HOST}/users/login/"


@given("I fill form field {field} with {value}")
def step_fill_form(context, field, value):
    context.form_data.update({field: value})


@when("I try to log in")
def step_try_to_log_in(context):
    context.response = httpx.post(SERVICE_ENDPOINT, json=context.form_data)


@then("it should return {status_code}")
def step_check_status_code(context, status_code):
    assert context.response.status_code == int(status_code)
