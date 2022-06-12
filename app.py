from aws_cdk import App, Stack
from aws_cdk import aws_apigateway as _apigw
from aws_cdk import aws_lambda as _lambda
from constructs import Construct

# pylint: disable=too-few-public-methods


class HelloLambdaStack(Stack):
    def __init__(self, scope: Construct, id_: str, **kwargs) -> None:
        super().__init__(scope, id_, **kwargs)

        base_lambda = _lambda.Function(
            self,
            "HelloLambda",
            handler="src/handlers/http/hello.handler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("src"),
        )

        base_api = _apigw.RestApi(self, "ApiGateway", rest_api_name="ApiGateway")

        example_entity = base_api.root.add_resource("hello")
        example_entity_lambda_integration = _apigw.LambdaIntegration(
            base_lambda,
            proxy=False,
            integration_responses=[_apigw.IntegrationResponse(status_code="200")],
        )
        example_entity.add_method(
            "GET",
            example_entity_lambda_integration,
            method_responses=[_apigw.MethodResponse(status_code="200")],
        )


app = App()
HelloLambdaStack(app, "HelloLambdaStack")
app.synth()
