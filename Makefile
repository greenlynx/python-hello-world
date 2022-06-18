install:
	pip install -r ./requirements-dev.txt

checks:
	pre-commit run --all-files

all-tests:
	pytest

unit-tests:
	pytest -m "not integration"

mutation-tests:
	mutmut run

deploy-non-prod:
	cdk deploy --hotswap --require-approval never

deploy:
	cdk deploy --require-approval never

get-deployed-api-url:
	tools/get-deployed-api-url.sh

get-deployed-host-name:
	make get-deployed-api-url -s | sed 's/https:\/\///' | sed 's/\/.*//'

get-deployed-path:
	make get-deployed-api-url -s | sed 's/\/$$//' | sed 's/.*\///'

zap-scan:
	tools/zap-scan.sh
