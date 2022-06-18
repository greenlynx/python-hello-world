#!/bin/sh
make deploy-non-prod
jq ".host = \"$(make -s get-deployed-host-name)\"" docs/openapi.json | jq ".basePath = \"/$(make -s get-deployed-path)\"" >docs/openapi.transformed.json
mkdir -p reports/zap
docker pull owasp/zap2docker-stable
docker run --user root -v "$(pwd)":/zap/wrk/:rw --network=host -t owasp/zap2docker-stable zap-api-scan.py -t docs/openapi.transformed.json -J reports/zap/results.json -w reports/zap/results.md -r reports/zap/results.html -f openapi -c .zap/rules.tsv
