# Zato ESB example

![Architecture diagram][architecture]

## Requirements

* [Docker Compose](https://docs.docker.com/compose/)

## Running example

sync events and translate apps:
```
$ git submodule sync --recursive
$ git submodule update --init --remote
```

run zato ESB, applications and tests:
```
$ docker-compose up
```

## Try it out

getting user token directry from users app:
```
$ curl -X POST -F "login=foo" -F "password=bar" http://localhost:5001/login
{ 
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6ImZvbyIsInNjb3BlcyI6WyJwaG90b3M6dmlldyJdLCJleHAiOjE1ODc0MDczOTR9.8Ftdkm31_GTCgM-JRo6btjnLVMDBU_sGdCF6m5VcLWM"
}
```

photo 1 is available for everyone, to check this type:

```
$ curl http://localhost:5002/photo/1
{
  "src": "https://via.placeholder.com/150/0000FF/808080"
}
```

but anonymous user cannot get photo with id 2:
```
$ curl http://localhost:5002/photo/2
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>403 Forbidden</title>
<h1>Forbidden</h1>
<p>You don't have the permission to access the requested resource. It is either read-protected or not readable by the server.</p>
```

Check if builtin zato PING service works:
```
$ curl http://localhost:11223/zato/ping
{
  "zato_ping_response": {
    "pong": "zato"
  },
  "zato_env": {
    "result": "ZATO_OK",
    "cid": "c80ebe3cb653c3f1a73e28e9",
    "details": ""
  }
}
```

call Login service and get token via ESB:
```
$ curl -X POST -d '{"login": "foo", "password": "bar"}' \
    http://localhost:11223/users/login/
{
  "status": "Login Successful",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6ImZvbyIsInNjb3BlcyI6WyJwaG90b3M6dmlldyJdLCJleHAiOjE1ODc0MDczOTR9.8Ftdkm31_GTCgM-JRo6btjnLVMDBU_sGdCF6m5VcLWM"
}
```
call get-photo service with given token:
```
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6ImZvbyIsInNjb3BlcyI6WyJwaG90b3M6dmlldyJdLCJleHAiOjE1ODc0MDgwNDd9.TgboV5Yy3zkXMx-xDvlwyljUXv2vEnFxEfWs0yaMmDQ" \
    http://localhost:11223/photos/get-photo/2/
{
  "src": "https://via.placeholder.com/150/FF0000/FFFFFF"
}
```
call Login service with invalid credentials and pass ACCEPT-LANGUAGE header:
```
curl -X POST \
    -d '{"login": "foo", "password": "wrong"}' \
    -H 'Accept-Language: pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7' \
    http://localhost:11223/users/login/
```

## Zato client

### Invoke service
invoke zato PING service from command line:
```
# zato service invoke /opt/zato/example/server1/ zato.ping
{'pong': 'zato'}
```

### Add channel connection
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
### Add outgoing connection
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
### Get HTTP or SOAP objects list by connection type
Connection type must be 'channel' or 'outgoing'.

```
# zato service invoke /opt/zato/example/server1 zato.http-soap.get-list --payload '{
    "cluster_id": 1,
    "connection": "outgoing"
}
```

[architecture]: https://github.com/kuter/zato-example/raw/master/architecture.png "Architecture"
