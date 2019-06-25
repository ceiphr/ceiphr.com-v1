#!/bin/bash

git pull
docker stop $(docker ps -aq)
# docker-compose -f docker-compose.prod.yml down -v  
docker-compose -f docker-compose.prod.yml up --build -d
