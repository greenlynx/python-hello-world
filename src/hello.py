import json

from aws_lambda_types.api_gw import APIGWPayloadV1RequestDict


def handler(
    event: APIGWPayloadV1RequestDict, context
):  # pylint: disable=unused-argument
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello world!", "foo": event["httpMethod"]}),
        "headers": {
            "X-Content-Type-Options": "nosniff",
            "Strict-Transport-Security": "max-age=63072000; includeSubDomains; preload",
        },
    }
