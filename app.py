import os
import pwd

from aws_cdk import App, Stack, aws_apigateway, aws_lambda, aws_lambda_python_alpha
from constructs import Construct

# pylint: disable=too-few-public-methods


def get_environment_name():
    if "DEPLOY_ENVIRONMENT" not in os.environ:
        return f"local-{pwd.getpwuid(os.getuid()).pw_name}"
    return os.environ["DEPLOY_ENVIRONMENT"]


class HelloLambdaStack(Stack):
    def __init__(self, scope: Construct, id_: str, **kwargs) -> None:
        super().__init__(scope, id_, **kwargs)

        hello_function = aws_lambda_python_alpha.PythonFunction(
            self,
            "HelloLambda",
            entry="./src",
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            index="hello.py",
            handler="handler",
        )

        aws_apigateway.LambdaRestApi(
            self,
            "HelloWorldApi",
            handler=hello_function,
            proxy=False,
            deploy_options=aws_apigateway.StageOptions(
                stage_name=get_environment_name()
            ),
        ).root.add_resource("hello").add_method("GET")


app = App()
HelloLambdaStack(app, f"HelloLambdaStack-{get_environment_name()}")
app.synth()
