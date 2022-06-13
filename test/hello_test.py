import json

from src.hello import handler


def test_it_says_hello():
    result = handler({"httpMethod": "a"})
    assert result["statusCode"] == 200
    assert result["body"] == json.dumps({"message": "Hello world!", "foo": "a"})
