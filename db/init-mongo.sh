#!/bin/bash
set -e

mongosh <<EOF
use admin 
db.createUser(
  {
    user: "${MONGO_INITDB_ROOT_USERNAME}",
    pwd: "${MONGO_INITDB_ROOT_PASSWORD}",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
)

use ${MONGO_INITDB_DATABASE}
db.createCollection("predictions")
EOF