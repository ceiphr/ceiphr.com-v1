#!/bin/bash

git pull
docker stop $(docker ps -aq)
docker system prune
docker-compose -f docker-compose.prod.yml up --build -d
