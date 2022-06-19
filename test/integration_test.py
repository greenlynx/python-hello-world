import json
import os

import pytest
import requests

pytestmark = pytest.mark.integration
CDK_OUTPUTS_FILE = "cdk.out/outputs.json"


@pytest.fixture(name="api_base_url")
def api_base_url_fixture():
    cdk_command = (
        "cdk deploy --all --hotswap  --require-approval never "
        f"--outputs-file {CDK_OUTPUTS_FILE}"
    )
    os.system(cdk_command)  # nosec B605

    with open(CDK_OUTPUTS_FILE, encoding="utf-8") as file:
        data = json.load(file)

    for stack in data:
        if stack.startswith("HelloLambdaStack-"):
            for output in data[stack]:
                if output.startswith("HelloWorldApiEndpoint"):
                    return data[stack][output]

    return ""


def test_get_hello_should_return_200(api_base_url):
    response = requests.get(f"{api_base_url}hello")
    assert response.status_code == 200
