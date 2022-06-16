# Python/Lambda 'hello world' example

![Build/test/deploy](https://github.com/greenlynx/python-hello-world/actions/workflows/main.yml/badge.svg)
![Nightly checks](https://github.com/greenlynx/python-hello-world/actions/workflows/nightly.yml/badge.svg)

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
pip install -r ./requirements-dev.txt   # install packages
pre-commit install                      # set up git hooks
```

## Run checks and unit tests

`pre-commit run --all-files`

## Run all tests (including integration)

Configure AWS credentials, then:

`pytest`

## Run mutation tests

`mutmut run`

## Deploy to your personal local environment

`cdk deploy`

## Deploy to another environment

`DEPLOY_ENVIRONMENT=dev cdk deploy`
