#!/bin/bash
CONTAINER=zato-example_zato_1
docker cp services/photos.py zato-example_zato_1:/opt/zato/example/server1/pickup/incoming/services

docker exec $CONTAINER zato service invoke /opt/zato/example/server1/ zato.http-soap.create --payload '{
    "cluster_id": 1,
    "name": "Get photo",
    "is_active": true,
    "is_internal": false,
    "url_path": "/photos/get-photo",
    "service": "photos.get-photo",
    "ping_method": "HEAD",
    "pool_size": 20,
    "timeout": 10,
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
    "timeout": "10"
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
    "timeout": "10"
}'
