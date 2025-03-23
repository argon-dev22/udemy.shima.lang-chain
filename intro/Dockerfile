FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /docker

RUN pip install --no-cache-dir nltk
COPY ./docker/init_nltk.py .
RUN python3 ./init_nltk.py

ARG APP_ROOT_NAME=app

ENV PYTHONPATH=/${APP_ROOT_NAME}

WORKDIR /${APP_ROOT_NAME}

COPY ./${APP_ROOT_NAME}/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./${APP_ROOT_NAME}/ .
