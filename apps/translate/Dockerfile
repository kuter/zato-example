FROM python:3.8-alpine
ENV PYTHONBUFFERED 1
RUN apk add make

RUN pip install pipenv
COPY Pipfile* /
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app
RUN pybabel compile -d translations

CMD ["flask", "run", "--host=0.0.0.0"]
