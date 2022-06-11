import json
import string

from api_gw import APIGWPayloadV2RequestContextDict, APIGWPayloadV2RequestDict


def handler(event: APIGWPayloadV2RequestDict, context: APIGWPayloadV2RequestContextDict):
    return {"statusCode": 200, "body": json.dumps({"message": "Hello world!", "path": event["rawPath"]})}
