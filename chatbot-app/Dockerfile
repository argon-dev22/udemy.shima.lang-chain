FROM python:3.11-slim


ENV alias py=python3


# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*


# Install Poetry
ENV HOME=/root
RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.8.4
ENV PATH="$HOME/.local/bin:$PATH"

# Install nltk
# WORKDIR /docker

# RUN pip install --no-cache-dir nltk
# COPY ./docker/init_nltk.py .
# RUN python3 ./init_nltk.py


ARG APP_ROOT_NAME=app

ENV PYTHONPATH=/${APP_ROOT_NAME}

WORKDIR /${APP_ROOT_NAME}

# Install libraries
COPY ./${APP_ROOT_NAME}/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY ./${APP_ROOT_NAME}/ .
