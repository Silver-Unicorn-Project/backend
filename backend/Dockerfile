FROM python:latest
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code/
COPY requirements.txt /code/
RUN apt-get update \
    && apt-get install -y python3-pip \
    && pip3 install --disable-pip-version-check -r requirements.txt \
    && apt-get remove -y python3-pip \
    && apt-get autoremove --purge -y \
    && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/*.list

COPY . /code/
