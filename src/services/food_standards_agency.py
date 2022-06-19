from os import environ
from typing import NamedTuple

import requests


class EstablishmentInfo(NamedTuple):
    name: str


def get_establishment_name(id_: str) -> EstablishmentInfo:
    fhrs_api_url = environ["FHRS_API_BASE_URL"]
    response = requests.get(
        f"{fhrs_api_url}?id={id_}",
        headers={"x-api-version": "2"},
    )
    response.raise_for_status()
    return response.json()["establishments"][0]["BusinessName"]
