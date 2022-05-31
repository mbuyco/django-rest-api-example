# syntax=docker/dockerfile:1
FROM python:3.8-alpine

RUN apk --update --no-cache add \
    build-base \
    libffi-dev \
    libpq \
    postgresql \
    postgresql-dev \
    python3-dev

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN python -m ensurepip
RUN pip install -r requirements.txt
COPY . /code/

