# Zato ESB example

## Requirements

* [Docker Compose](https://docs.docker.com/compose/)
* [git-subrepo](https://github.com/ingydotnet/git-subrepo)

## Running example
```
$ git subrepo pull --all
$ docker-compose up
```

and setup up services:

```
$ sh install.sh
```

## Check if PING service works
```
$ curl http://localhost:11223/zato/ping ; echo
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

## How to test if that works

photo 1 is available for everyone, to check this type:

```
$ curl http://localhost:5002/photo/1
{
  "src": "https://via.placeholder.com/150/0000FF/808080"
}
```

getting user token:

```
$ curl -X POST -F "login=foo" -F "password=bar" http://localhost:5001/login
{
    "first_name": "foo", 
    "last_name": "bar", 
    "token": "bed4c91860374151ad2f2676ded55a52"
}
```

call get-photo service via ESB with credentials and get photo for logged users only:

```
$ curl http://localhost:11223/photos/get-photo/2/ -d '{"login": "foo", "password": "bar"}'
{
  "src": "https://via.placeholder.com/150/FF0000/FFFFFF"
}
```

getting user token via ESB:

```
curl -X POST http://localhost:11223/users/login/ -d '{"login": "foo", "password": "bar"}'
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
