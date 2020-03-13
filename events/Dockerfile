FROM python:3.8-alpine

RUN apk add build-base

COPY requirements/ /

COPY . /app
WORKDIR /app

RUN pip install -r requirements/base.txt
RUN alembic upgrade head

CMD ["uvicorn", "events.main:app", "--host", "0.0.0.0", "--reload"]
