import pook
from pytest_mock import MockerFixture

from src.services.food_standards_agency import get_establishment_name


@pook.on
def test_it_works(mocker: MockerFixture):
    mocker.patch(
        "src.services.food_standards_agency.environ",
        {"FHRS_API_BASE_URL": "https://stubbed_url"},
    )
    pook.get("https://stubbed_url").param("id", "123").header(
        "x-api-version", "2"
    ).reply(200).json({"establishments": [{"BusinessName": "foo"}]})

    result = get_establishment_name("123")

    assert result == "foo"
