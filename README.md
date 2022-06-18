# Python/Lambda 'hello world' example

![Lint/test/deploy](https://github.com/greenlynx/python-hello-world/actions/workflows/main.yml/badge.svg)
![Nightly checks](https://github.com/greenlynx/python-hello-world/actions/workflows/nightly.yml/badge.svg)

This is a small 'hello world' example I've been using to experiment with building a simple Python lambda, and trying out some of the tooling in the Python ecosystem.

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

## Run API security tests (ZAP scan)

`make zap-scan`

## Run mutation tests

`make mutation-tests`

## Deploy to your personal local environment

`make deploy`

## Deploy to another environment

`DEPLOY_ENVIRONMENT=dev make deploy`
