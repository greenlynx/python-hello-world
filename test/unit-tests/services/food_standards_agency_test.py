import pook

from src.services.food_standards_agency import get_establishment_name


@pook.on
def test_it_works():
    pook.get("https://api.ratings.food.gov.uk/establishments/list").param(
        "id", "123"
    ).header("x-api-version", "2").reply(200).json(
        {"establishments": [{"BusinessName": "foo"}]}
    )

    result = get_establishment_name("123")

    assert result == "foo"
