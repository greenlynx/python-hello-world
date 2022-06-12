import json

# sys.path.append(r"../src")
from src.hello_world_service.handlers.http import hello


def test_it_says_hello():
    result = hello.handler({"rawQueryString": "a"}, {"domainName": "b"})
    assert result["statusCode"] == 200 and result["body"] == json.dumps(
        {"message": "Hello world!", "foo": "a", "bar": "b"}
    )
