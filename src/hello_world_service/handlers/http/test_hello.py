import json

import hello


def test_it_says_hello():
    result = hello.handler({"rawQueryString": "a"}, {"domainName": "b"})
    assert result["statusCode"] == 200 and result["body"] == json.dumps(
        {"message": "Hello world!", "foo": "a", "bar": "b"}
    )
