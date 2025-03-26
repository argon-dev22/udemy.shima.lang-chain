FROM python:3.11-slim


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


ARG APP_ROOT_NAME=app

ENV PYTHONPATH=/${APP_ROOT_NAME}

WORKDIR /${APP_ROOT_NAME}

# Install libraries
COPY ./${APP_ROOT_NAME}/pyproject.toml ./${APP_ROOT_NAME}/poetry.lock ./
RUN poetry install

# Copy the application code
COPY ./${APP_ROOT_NAME}/ .


# Set alias
RUN echo "alias py=python3" >> ~/.bashrc
RUN echo "alias po=poetry" >> ~/.bashrc
RUN echo "alias popy='poetry run python'" >> ~/.bashrc

WORKDIR /${APP_ROOT_NAME}/src/

CMD ["poetry", "run", "python", "-u", "main.py"]