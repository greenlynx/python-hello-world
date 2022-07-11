import json
import os

import pytest
import requests

pytestmark = pytest.mark.integration
CDK_OUTPUTS_FILE = "cdk.out/outputs.json"
INTEGRATION_TEST_API_KEY = "testtesttesttesttest"


@pytest.fixture(name="api_outputs")
def api_outputs_fixture():
    cdk_command = (
        "cdk deploy --all --require-approval never --hotswap --no-rollback "
        f"--outputs-file {CDK_OUTPUTS_FILE}"
    )
    if os.system(cdk_command) != 0:  # nosec B605
        pytest.fail("CDK deployment failed, please check the logs")

    with open(CDK_OUTPUTS_FILE, encoding="utf-8") as file:
        data = json.load(file)

    for stack in data:
        if stack.startswith("HelloWorldStack-"):
            api_key = data[stack]["ApiKey"]
            for output in data[stack]:
                if output.startswith("HelloWorldApi"):
                    api_url = data[stack][output]

    if not api_key:
        raise Exception(f"Could not get API key from {CDK_OUTPUTS_FILE}")
    if not api_url:
        raise Exception(f"Could not get API url from {CDK_OUTPUTS_FILE}")

    return {"api_key": api_key, "api_url": api_url}


def test_get_hello_should_return_200(api_outputs):
    response = requests.get(
        f"{api_outputs['api_url']}hello",
        headers={"x-api-key": api_outputs["api_key"]},
    )
    assert response.status_code == 200
