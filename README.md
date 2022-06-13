# Python/Lambda 'hello world' example

![Build/test/deploy](https://github.com/greenlynx/python-hello-world/actions/workflows/main.yml/badge.svg)

## Prerequisites

-   NodeJS v14+ (for CDK)
-   Docker (for CDK)
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

## Run mutation tests

`mutmut run`

## Generate CloudFormation

`cdk synth`

## Deploy

`cdk deploy`
