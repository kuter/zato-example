from behave import given, then, when


@then("it should return {status_code}")
def step_check_status_code(context, status_code):
    assert context.response.status_code == int(
        status_code
    ), f"{context.response.status_code} != {status_code}"
