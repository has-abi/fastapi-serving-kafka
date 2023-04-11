SHELL := /bin/bash

.PHONY: pipenv-env
pipenv-env: ## Create python environment
	pip install --upgrade pip
	pip install pipenv
	pipenv shell

.PHONY: install
install: ## Install project dependencies
	pipenv install --dev
	python -m spacy download en_core_web_sm

.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ \
	{ printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) }\
	 ' $(MAKEFILE_LIST)
