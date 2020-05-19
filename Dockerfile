FROM python:3.8.2-alpine

RUN apk add gcc musl-dev libffi-dev openssl-dev

COPY . /app
WORKDIR /app

# the datalake uses poetry for package management
RUN pip install poetry awscli

RUN poetry install

RUN /bin/sh
