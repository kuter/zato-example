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


@given("I logged in")
def step_Im_logged_in(context):
    payload = {"login": "foo", "password": "bar"}
    context.response = httpx.post(SERVICE_ENDPOINT, json=payload)
    token = context.response.json()["token"]
    context.headers = {"authorization": f"Bearer {token}"}
