from typing import NamedTuple

import requests


class EstablishmentInfo(NamedTuple):
    name: str


def get_establishment_name(id_: str) -> EstablishmentInfo:
    response = requests.get(
        f"https://api.ratings.food.gov.uk/establishments/list?id={id_}",
        headers={"x-api-version": "2"},
    )
    response.raise_for_status()
    return response.json()["establishments"][0]["BusinessName"]
