# Zato ESB example

![Architecture diagram][architecture]



## Requirements

* [Docker Compose](https://docs.docker.com/compose/)
* [git-subrepo](https://github.com/ingydotnet/git-subrepo)

## Running example

sync events and translate apps:
```
$ git submodule sync --recursive
$ git submodule update --init --remote
```

run zato ESB, applications and run tests:
```
$ docker-compose up
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

## Add channel connection
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

## Add outgoing connection
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
curl -X POST \
    -d '{"login": "foo", "password": "bar"}' \
    http://localhost:11223/users/login/
```

call Login service with invalid credentials and pass ACCEPT-LANGUAGE header:

```
curl -X POST \
    -d '{"login": "foo", "password": "wrong"}' \
    -H 'Accept-Language: pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7' \
    http://localhost:11223/users/login/
```

[architecture]: https://github.com/kuter/zato-example/raw/master/architecture.png "Architecture"
