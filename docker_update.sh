#!/bin/bash

git pull
docker stop $(docker ps -aq)
docker-compose -f docker-compose.prod.yml up --build --env-file .env -d
