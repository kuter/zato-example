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

or invoke service from command line:

```
# zato service invoke /opt/zato/example/server1/ zato.ping
{'pong': 'zato'}
```

## Hot deploying first service

```
$ docker cp services/my_service.py zato-example_zato_1:/opt/zato/example/server1/pickup/incoming/services
```

## Get HTTP or SOAP objects list by connection type

Connection type must be 'channel' or 'outgoing'

```
# zato service invoke /opt/zato/example/server1 zato.http-soap.get-list --payload '{"cluster_id": 1, "connection": "outgoing"}'
```

## Add ongoing connection

```
# zato service invoke /opt/zato/example/server1/ zato.http-soap.create --payload '{   
    "cluster_id": 1,
    "name": "CRM",
    "is_internal": false,
    "is_active": true,
    "connection": "outgoing",
    "transport": "plain_http",
    "url_path": "/get-customer",
    "host": "http://tutorial.zato.io",
    "ping_method": "HEAD",
    "pool_size": 20, 
    "timeout": "10"
}'
```

## Debugging with wdb

install wdb inside container:

```
$ docker exec -it zato-example_users_1 pip install wdb
```

set breakpoint in your code:

```
$ import wdb; wdb.set_trace()
```

now you can access http://localhost:1984 via browser:

```
$ xdg-open http://localhost:1984
```
