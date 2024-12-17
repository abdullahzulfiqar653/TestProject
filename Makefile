.PHONY: services
services:
	test -f .env || touch .env
	docker-compose -f docker-compose.local.yml up --build