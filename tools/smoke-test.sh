#!/bin/sh
set -e
curl "$(make get-deployed-api-url -s)/hello"
