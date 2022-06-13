from aws_cdk import App, Stack, aws_apigateway, aws_lambda, aws_lambda_python_alpha
from constructs import Construct

# pylint: disable=too-few-public-methods


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
            self, "HelloWorldApi", handler=hello_function, proxy=False
        ).root.add_resource("hello").add_method("GET")


app = App()
HelloLambdaStack(app, "HelloLambdaStack")
app.synth()
