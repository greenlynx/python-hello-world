#!/bin/bash
set -e
ENVIRONMENT="${DEPLOY_ENVIRONMENT:-local-$USER}"
aws cloudformation describe-stacks --stack-name="HelloWorldStack-$ENVIRONMENT" --query "Stacks[0].Outputs" --output json | jq -rc '.[] | select(.OutputKey | test(".*HelloWorldApi.*Endpoint.*")) | .OutputValue'
