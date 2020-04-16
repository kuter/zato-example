# type: ignore
import os

import httpx
from behave import given, then, when

ZATO_HOST = os.getenv("ZATO_HOST", "http://zato:11223")
SERVICE_ENDPOINT = f"{ZATO_HOST}/users/login/"


@given("accept language header {language}")
def step_set_headers(context, language):
    context.headers = {"accept-language": language}


@when("I failed to log in")
def step_fail_to_log_in(context):
    payload = {"login": "invalid", "password": "invalid"}
    context.response = httpx.post(
        SERVICE_ENDPOINT, json=payload, headers=context.headers
    )


@when("I log in")
def step_impl(context):
    payload = {"login": "foo", "password": "bar"}
    context.response = httpx.post(
        SERVICE_ENDPOINT, json=payload, headers=context.headers
    )


@then("I should get response {response}")
def step_check_response(context, response):
    text = context.response.content.decode("utf-8")
    assert text == response, f"{text} != {response}"
