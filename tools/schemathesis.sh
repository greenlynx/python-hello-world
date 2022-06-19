#!/bin/sh
make deploy-non-prod
docker run --pull always --user root -v "$(pwd)":/code/:rw --network=host -t schemathesis/schemathesis:stable run /code/docs/openapi.json --checks all --code-sample-style python --base-url "$(make get-deployed-api-url -s)"
