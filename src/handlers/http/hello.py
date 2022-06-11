import json

from api_gw import (
    APIGWPayloadV2RequestContextDict,
    APIGWPayloadV2RequestDict,
    APIGWPayloadV2ResponseDict,
)


def handler(
    event: APIGWPayloadV2RequestDict, context: APIGWPayloadV2RequestContextDict
) -> APIGWPayloadV2ResponseDict:
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello world!"}),
    }
