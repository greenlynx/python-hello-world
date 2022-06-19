import json

from services.food_standards_agency import get_establishment_name


def handler(event, context):  # pylint: disable=unused-argument
    establishment_name = get_establishment_name(1)
    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"Hello {establishment_name}!"}),
        "headers": {
            "X-Content-Type-Options": "nosniff",
            "Strict-Transport-Security": "max-age=63072000; includeSubDomains; preload",
        },
    }
