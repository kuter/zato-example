# Zato ESB example

## Running example
```
$ docker-compose up
```

and setup `users` and `photos` services:

```
$ sh install.sh
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

## Add channel for that connection
```
# zato service invoke /opt/zato/example/server1/ zato.http-soap.create --payload '{
    "cluster_id": 1,
    "name": "Get Client Details",
    "is_active": true,
    "is_internal": false,
    "url_path": "/tutorial/first-service",
    "service": "my-service.get-client-details",
    "ping_method": "HEAD",
    "pool_size": 20,
    "timeout": 10,
    "connection": "channel",
    "transport": "plain_http"
}'
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

## Get HTTP or SOAP objects list by connection type
Connection type must be 'channel' or 'outgoing'.

```
# zato service invoke /opt/zato/example/server1 zato.http-soap.get-list --payload '{
    "cluster_id": 1,
    "connection": "outgoing"
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
