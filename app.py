from aws_cdk import App, Stack, aws_apigateway, aws_lambda
from constructs import Construct

# pylint: disable=too-few-public-methods


class HelloLambdaStack(Stack):
    def __init__(self, scope: Construct, id_: str, **kwargs) -> None:
        super().__init__(scope, id_, **kwargs)

        baseaws_lambda = aws_lambda.Function(
            self,
            "HelloLambda",
            handler="hello.handler",
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            code=aws_lambda.Code.from_asset("src"),
        )

        base_api = aws_apigateway.RestApi(
            self, "ApiGateway", rest_api_name="ApiGateway"
        )

        example_entity = base_api.root.add_resource("hello")
        example_entityaws_lambda_integration = aws_apigateway.LambdaIntegration(
            baseaws_lambda,
            proxy=False,
            integration_responses=[
                aws_apigateway.IntegrationResponse(status_code="200")
            ],
        )
        example_entity.add_method(
            "GET",
            example_entityaws_lambda_integration,
            method_responses=[aws_apigateway.MethodResponse(status_code="200")],
        )


app = App()
HelloLambdaStack(app, "HelloLambdaStack")
app.synth()
