[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

# FastAPI Events

## Instalation

Create and activate virtualenv first:

```
$ virtualenv -p python3 ~/virtualenvs/fastapi-events
$ source ~/virtualenv/fastapi-events/bin/activate
```

then install dev requirements:

```
$ pip install -r requirements/dev.txt
```

and make database migration:

```
$ alembic upgrade head
```

## Running project

```
$ uvicorn events.main:app --reload
```

## Example usage

create event first:

```
$ curl -X POST -d '{"event": "test event"}' http://localhost:8000/events/
```

get events list:

```
$ curl http://localhost:8000/events/
```
