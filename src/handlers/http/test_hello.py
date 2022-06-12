import json

import hello


def test_it_says_hello():
    result = hello.handler({}, {})
    assert result["statusCode"] == 200
    assert result["body"] == json.dumps({"message": "Hello world!!"})
