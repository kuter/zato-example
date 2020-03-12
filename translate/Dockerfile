FROM python:3.8-alpine

RUN apk add make

COPY requirements.txt /

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN make compile

CMD ["flask", "run", "--host=0.0.0.0"]
