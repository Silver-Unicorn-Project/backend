DC = docker compose
APP_FILE = docker-compose.yaml

.PHONY: app
app:
	${DC} -f ${APP_FILE} up -d

.PHONY: drop-app
drop-app:
	${DC} -f ${APP_FILE} down
