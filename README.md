# Python/Lambda 'hello world' example

![Lint/test/deploy](https://github.com/greenlynx/python-hello-world/actions/workflows/main.yml/badge.svg)
![Nightly checks](https://github.com/greenlynx/python-hello-world/actions/workflows/nightly.yml/badge.svg)

This is a small 'hello world' example I've been using to experiment with building a simple Python lambda, and trying out some of the tooling in the Python ecosystem.

![Architecture diagram](diagram.png)

## Prerequisites

-   NodeJS v14+ (for CDK)
-   Docker (for CDK)
-   AWS CLI
-   Python 3.9

## Getting started

```
npm install -g aws-cdk                  # install CDK CLI tool
python -m venv .venv                    # create virtual environment
source .venv/bin/activate               # activate virtual environment
make install                            # install packages
pre-commit install                      # set up git hooks
```

## Run checks and unit tests

`make checks`

## Run all tests (including integration)

Configure AWS credentials, then:

`make all-tests`

Code will be automatically deployed to your personal local environment

## Run schema tests (Schemathesis)

These tests ensure that the OpenAPI spec matches the API's actual schema, and also perform some fuzz testing against the API.

`make schemathesis`

## Run API security tests (ZAP scan)

These tests scan the API for security issues.

`make zap-scan`

## Run mutation tests

These tests introduce "mutations" into the codebase to check that the unit tests cover everything they should be covering.
`make mutation-tests`

## Deploy to your personal local environment

This deploys the code to your own, personal environment in AWS, so you can run tests against it without impacting other developers.

`make deploy`

## Deploy to another environment

`DEPLOY_ENVIRONMENT=dev make deploy`
