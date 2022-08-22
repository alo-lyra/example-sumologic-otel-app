DC = "docker-compose"

.PHONY: build
build:
	$(DC) build

.PHONY: up
up: down build
	$(DC) up -d

.PHONY: down
down:
	$(DC) stop

.PHONY: clean
clean: down
	$(DC) rm -f

.PHONY: clean_all
clean_all: clean down
	$(DC) down -v

.PHONY: env
env:
	cp -i .env.example .env

.PHONY: shell
shell:
	$(DC) run demo-server /bin/bash

# .PHONY: run
# run:
# 	$(COMPOSE) run --rm "$@"
