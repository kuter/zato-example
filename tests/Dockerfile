FROM python:3.8-alpine
RUN apk add bash

COPY requirements.txt /

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
