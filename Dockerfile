FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

WORKDIR /languages

COPY Pipfile Pipfile.lock /languages/
RUN pip install pipenv && pipenv install --system

COPY . /languages/