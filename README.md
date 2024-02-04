# silver_unicorn

[![](https://github.com/Olesyacur/silver_unicorn/actions/workflows/flake8.yml/badge.svg?branch=main)](https://github.com/Olesyacur/silver_unicorn/actions/workflows/flake8.yml)

## Интернет-магазин товаров для любителей конного спорта


### Как запустить:

Файл envExample переименовать в .env. Поменять значения переменных окружения в соответствии со своими параметрами системы

#### Локально

***!!!Сервер БД при этом нужно поднять самостоятельно и указать в файле .env параметры подключения!!!***

Для запуска локально на unix выполнить команду:

```bash
make local-app
```

Для запуска под windows выполнить следующие команды:

```bash
pip install -r requirements.txt
python ./backend/manage.py migrate
python ./backend/manage.py collectstatic
python ./backend/manage.py runserver 0.0.0.0:8000
```

Сервис будет доступен по адресу http://localhost:8000

#### В docker контейнере

Для запуска в docker на unix выполнить команду:

```bash
make docker-app
```

Для запуска в docker под windows выполнить следующие команды:

**Если честно - не знаю, допишите кто в курсе, ни разу докер под виндой не стартовал...**

Для остановки docker контейнера:

```bash
make drop-docker-app
```
