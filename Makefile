DC = docker compose
APP_FILE = docker-compose.yaml

.PHONY: docker-app
docker-app:
	${DC} -f ${APP_FILE} up -d

.PHONY: drop-docker-app
drop-docker-app:
	${DC} -f ${APP_FILE} down

.PHONY: local-app
local-app:
	pip install -r requirements.txt
	python ./backend/manage.py migrate --noinput
	python ./backend/manage.py collectstatic --noinput
	python ./backend/manage.py runserver 0.0.0.0:8000

