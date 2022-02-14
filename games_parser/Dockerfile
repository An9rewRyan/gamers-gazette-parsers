FROM python:3.9-slim

ARG DEBIAN_FRONTEND="noninteractive"

WORKDIR /news_parser
COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN apt-get update \
#     && apt-get install -y libpq-dev gcc python3-dev musl-dev
COPY . Pipfile Pipfile.lock /news_parser/

RUN python -m pip install --upgrade pip \
    && pip install pipenv 

# RUN apt-get install -y netcat

RUN pipenv install --system --deploy --ignore-pipfile 

COPY . /news_parser/
