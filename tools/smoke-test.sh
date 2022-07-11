#!/bin/sh
set -e
URL="$(make get-deployed-api-url -s)hello"
API_KEY="$(make get-deployed-api-key-value -s)"
echo "$URL"
curl -H "x-api-key: $API_KEY" "$URL" --fail
