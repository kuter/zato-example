#!/bin/bash
ZATO_DIR=/opt/zato/example
rm -rf $ZATO_DIR
mkdir $ZATO_DIR
zato quickstart create $ZATO_DIR sqlite redis 6379 --cluster_name zato-example --servers 1
sed -i 's/127.0.0.1:11223/0.0.0.0:11223/g' "$ZATO_DIR/load-balancer/config/repo/zato.config"
sed -i 's/pickup_dir=.*/pickup_dir=\/incoming\/services/g' "$ZATO_DIR/server1/config/repo/server.conf"

$ZATO_DIR/zato-qs-start.sh
zato update password "$ZATO_DIR/web-admin/" admin --password admin

find /incoming/services -type f -exec touch {} +

services=`cat services.json | jq -c '.[]'`
for service in $services; do
    zato service invoke "$ZATO_DIR/server1/" zato.http-soap.create --payload "$service"
done

tail -f "$ZATO_DIR/server1/logs/server.log"
