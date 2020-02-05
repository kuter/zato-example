# Zato ESB example

## Running example

```
$ docker-compose up
```

## Check if PING service works

```
$ curl localhost:11223/zato/ping ; echo
{"zato_ping_response": {"pong": "zato"}, "zato_env": {"result": "ZATO_OK", "cid": "dd334d37c15369008aa42e92", "details": ""}}
```
