SHELL := /bin/bash

.PHONY: kafka-cluster
kafka-cluster: ## Start Kafka cluster
	docker-compose up -d --build zookeeper kafka

.PHONY: mongodb
mongodb: ## Start mongodb
	docker-compose up -d --build mongodb

.PHONY: serving-service
serving-service: ## Start serving service with kafka cluster
	docker-compose up -d --build zookeeper kafka serving-service

.PHONY: data-service
data-service: ## Start data service with kafka cluster and mongodb
	docker-compose up -d --build mongodb zookeeper kafka data-service

.PHONY: all
all: ## Start all services
	docker-compose up -d --build

.PHONY: down
down: ## Stop all services
	docker-compose down

.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ \
	{ printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) }\
	 ' $(MAKEFILE_LIST)