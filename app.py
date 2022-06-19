import os
import pwd

from aws_cdk import (
    App,
    Aspects,
    Stack,
    aws_apigateway,
    aws_lambda,
    aws_lambda_python_alpha,
    aws_logs,
)
from cdk_nag import AwsSolutionsChecks, NagSuppressions
from constructs import Construct

# pylint: disable=too-few-public-methods

app = App()

Aspects.of(app).add(AwsSolutionsChecks(verbose=True))
non_test_environments = ["dev", "test", "staging", "prod"]

if os.environ["DEPLOY_ENVIRONMENT"] not in non_test_environments:
    environment_name = f"local-{pwd.getpwuid(os.getuid()).pw_name}"
else:
    environment_name = os.environ["DEPLOY_ENVIRONMENT"]


IS_TEST_ENVIRONMENT = environment_name not in non_test_environments


if IS_TEST_ENVIRONMENT:

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

    test_stubs_stack = TestStubsStack(
        app, f"HelloLambdaTestStubsStack-{environment_name}"
    )
    NagSuppressions.add_stack_suppressions(
        test_stubs_stack,
        [
            {"id": "AwsSolutions-IAM4", "reason": "TODO: tighten up permissions"},
        ],
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

        api = aws_apigateway.LambdaRestApi(
            self,
            "HelloWorldApi",
            handler=hello_function,
            proxy=False,
            deploy_options=aws_apigateway.StageOptions(
                stage_name=environment_name,
                access_log_destination=aws_apigateway.LogGroupLogDestination(
                    aws_logs.LogGroup(self, "ApiGatewayAccessLogsTODO")
                ),
                logging_level=aws_apigateway.MethodLoggingLevel.INFO,
            ),
        )
        api.root.add_resource("hello").add_method(
            "GET",
            request_validator_options={
                "validate_request_parameters": True,
            },
        )


main_stack = HelloLambdaStack(app, f"HelloLambdaStack-{environment_name}")
NagSuppressions.add_stack_suppressions(
    main_stack,
    [
        {"id": "AwsSolutions-IAM4", "reason": "TODO: tighten up permissions"},
        {"id": "AwsSolutions-APIG3", "reason": "TODO: implement WAF"},
        {"id": "AwsSolutions-APIG4", "reason": "API auth not needed"},
        {"id": "AwsSolutions-COG4", "reason": "Cognito not in use"},
    ],
)


app.synth()
