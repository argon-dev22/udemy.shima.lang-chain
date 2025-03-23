FROM python:3.11-slim

ARG APP_ROOT_NAME=app

ENV PYTHONPATH=/${APP_ROOT_NAME}

WORKDIR /${APP_ROOT_NAME}

COPY ./${APP_ROOT_NAME}/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./${APP_ROOT_NAME}/ .
