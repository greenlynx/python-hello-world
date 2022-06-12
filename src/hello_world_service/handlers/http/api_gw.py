from typing import Dict, List

from typing_extensions import Literal, TypedDict


class APIGWPayloadV2RequestContextHTTPDict(TypedDict):
    method: str
    path: str
    protocol: str
    sourceIp: str
    userAgent: str


class APIGWPayloadV2RequestContextDict(TypedDict):
    accountId: str
    apiId: str
    domainName: str
    domainPrefix: str
    http: APIGWPayloadV2RequestContextHTTPDict
    requestId: str
    routeKey: str
    stage: str
    time: str
    timeEpoch: int


class APIGWPayloadV2RequestDict(TypedDict):
    body: str
    cookies: List[str]
    headers: Dict[str, str]
    isBase64Encoded: bool
    queryStringParameters: Dict[str, str]
    rawPath: str
    rawQueryString: str
    requestContext: APIGWPayloadV2RequestContextDict
    routeKey: str
    version: Literal["2.0"]


class APIGWPayloadV2ResponseDict(TypedDict):
    # cookies: List[str]
    # isBase64Encoded: bool
    statusCode: int
    # headers: Dict[str, str]
    body: str
