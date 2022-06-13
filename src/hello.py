import json

from aws_lambda_types.api_gw import APIGWPayloadV1RequestDict


def handler(event: APIGWPayloadV1RequestDict):
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello world!", "foo": event["httpMethod"]}),
    }
