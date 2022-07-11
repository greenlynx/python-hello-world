#!/bin/bash
set -e
ENVIRONMENT="${DEPLOY_ENVIRONMENT:-local-$USER}"
API_KEY_ID=$(aws cloudformation describe-stacks --stack-name="HelloWorldStack-$ENVIRONMENT" --query "Stacks[0].Outputs" --output json | jq -rc '.[] | select(.OutputKey | test("ApiKeyId")) | .OutputValue')
aws apigateway get-api-key --api-key "$API_KEY_ID" --include-value --output=json | jq -r ".value"
