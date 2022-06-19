#!/bin/sh
set -e
URL="$(make get-deployed-api-url -s)/hello"
echo "$URL"
curl "$URL" --fail
