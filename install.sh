#!/bin/bash
CONTAINER=zato-example_zato_1
docker cp services/photos.py $CONTAINER:/opt/zato/example/server1/pickup/incoming/services

docker exec $CONTAINER zato service invoke /opt/zato/example/server1/ zato.http-soap.create --payload '{
    "cluster_id": 1,
    "name": "Get photo",
    "is_active": true,
    "is_internal": false,
    "url_path": "/photos/get-photo/{photo_id}/",
    "service": "photos.get-photo",
    "ping_method": "HEAD",
    "pool_size": 20,
    "timeout": 3600,
    "connection": "channel",
    "transport": "plain_http"
}'

docker cp services/users.py $CONTAINER:/opt/zato/example/server1/pickup/incoming/services
docker exec $CONTAINER zato service invoke /opt/zato/example/server1/ zato.http-soap.create --payload '{
    "cluster_id": 1,
    "name": "Login",
    "is_active": true,
    "is_internal": false,
    "url_path": "/users/login/",
    "service": "users.login",
    "ping_method": "HEAD",
    "pool_size": 20,
    "timeout": 3600,
    "connection": "channel",
    "transport": "plain_http"
}'


docker exec $CONTAINER zato service invoke /opt/zato/example/server1/ zato.http-soap.create --payload '{
    "cluster_id": 1,
    "name": "Login",
    "is_internal": true,
    "is_active": true,
    "connection": "outgoing",
    "transport": "plain_http",
    "url_path": "/login",
    "host": "http://users:5000",
    "ping_method": "HEAD",
    "pool_size": 20,
    "timeout": "3600"
}'

docker exec $CONTAINER zato service invoke /opt/zato/example/server1/ zato.http-soap.create --payload '{
    "cluster_id": 1,
    "name": "Photo",
    "is_internal": true,
    "is_active": true,
    "connection": "outgoing",
    "transport": "plain_http",
    "url_path": "/photo/{photo_id}",
    "host": "http://photos:5000",
    "ping_method": "HEAD",
    "pool_size": 20,
    "timeout": "3600"
}'
