import json

from src.hello import handler


def test_it_says_hello():
    result = handler({"httpMethod": "a"}, {})
    assert result["statusCode"] == 200
    assert result["body"] == json.dumps({"message": "Hello world!", "foo": "a"})
    assert result["headers"]["X-Content-Type-Options"] == "nosniff"
    assert (
        result["headers"]["Strict-Transport-Security"]
        == "max-age=63072000; includeSubDomains; preload"
    )
