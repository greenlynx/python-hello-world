import os
import pwd

from aws_cdk import App, Stack, aws_apigateway, aws_lambda, aws_lambda_python_alpha
from constructs import Construct

# pylint: disable=too-few-public-methods

app = App()

non_test_environments = ["dev", "staging", "prod"]

if "DEPLOY_ENVIRONMENT" not in non_test_environments:
    environment_name = f"local-{pwd.getpwuid(os.getuid()).pw_name}"
else:
    environment_name = os.environ["DEPLOY_ENVIRONMENT"]


IS_TEST_ENVIRONMENT = environment_name not in non_test_environments


class TestStubsStack(Stack):
    def __init__(self, scope: Construct, id_: str, **kwargs) -> None:
        super().__init__(scope, id_, **kwargs)

        self.food_standards_agency_url = (
            aws_lambda_python_alpha.PythonFunction(
                self,
                "HelloLambda",
                entry="./test/stubs",
                runtime=aws_lambda.Runtime.PYTHON_3_9,
                index="food_standards_agency.py",
                handler="handler",
            )
            .add_function_url(auth_type=aws_lambda.FunctionUrlAuthType.NONE)
            .url
        )

    def get_food_standards_agency_url(self):
        return self.food_standards_agency_url


if IS_TEST_ENVIRONMENT:
    test_stubs_stack = TestStubsStack(
        app, f"HelloLambdaTestStubsStack-{environment_name}"
    )
    environment_variables = {
        "FHRS_API_BASE_URL": test_stubs_stack.get_food_standards_agency_url()
    }
else:
    if environment_name == "dev":
        environment_variables = {
            "FHRS_API_BASE_URL": "https://api.ratings.food.gov.uk/establishments/list"
        }
    else:
        raise f"Unknown environment {environment_name}"


class HelloLambdaStack(Stack):
    def __init__(self, scope: Construct, id_: str, **kwargs) -> None:
        super().__init__(scope, id_, **kwargs)

        hello_function = aws_lambda_python_alpha.PythonFunction(
            self,
            "HelloLambda",
            entry="./src",
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            index="handlers/hello.py",
            handler="handler",
            environment=environment_variables,
        )

        aws_apigateway.LambdaRestApi(
            self,
            "HelloWorldApi",
            handler=hello_function,
            proxy=False,
            deploy_options=aws_apigateway.StageOptions(stage_name=environment_name),
        ).root.add_resource("hello").add_method("GET")


HelloLambdaStack(app, f"HelloLambdaStack-{environment_name}")

app.synth()
