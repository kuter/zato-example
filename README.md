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

## Hot deploying first service

```
$ docker cp services/my_service.py zato-example_zato_1:/opt/zato/example/server1/pickup/incoming/services
```

## Debugging with wdb

install inside container:

```
$ docker exec -it zato-example_users_1 pip install wdb
```

set breakpoint:

```
$ import wdb; wdb.set_trace()
```

now you can access http://localhost:1984 via browser:

```
$ xdg-open http://localhost:1984
```
