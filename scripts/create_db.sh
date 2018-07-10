#!/usr/bin/env bash

commands=(
  "CREATE DATABASE $1;"
  "CREATE USER $2 WITH PASSWORD '$3';"
  "GRANT ALL PRIVILEGES ON DATABASE $1 TO $2;"
  "ALTER USER $2 CREATEDB;"
)

if [ $(uname) == "Darwin" ]
then
for command in "${commands[@]}"; do psql postgres -c "$command"; done
else
for command in "${commands[@]}"; do sudo -u postgres psql -c "$command"; done
fi
