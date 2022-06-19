import json

from pytest_mock import MockerFixture

from src.handlers.hello import handler


def test_it_says_hello(mocker: MockerFixture):
    mocker.patch(
        "src.handlers.hello.get_establishment_name",
        lambda id: "world" if id == 1 else "",
    )

    result = handler({}, {})
    assert result["statusCode"] == 200
    assert result["body"] == json.dumps({"message": "Hello world!"})
    assert result["headers"]["X-Content-Type-Options"] == "nosniff"
    assert (
        result["headers"]["Strict-Transport-Security"]
        == "max-age=63072000; includeSubDomains; preload"
    )
