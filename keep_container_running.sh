#!/bin/bash

# Schedule this script using crontab
# 0 0 * * * bash /home/siddharth/excerpts_bot/keep_container_running.sh

cd /home/siddharth/excerpts_bot

echo "START"
date +"%F %R"

echo "STEP: Restarting container"

docker container stop excerpts
docker container rm excerpts
docker build . -t excerpts:latest
docker run -d --name excerpts excerpts:latest

echo "STEP: Container restarted"

date +"%F %R"
echo "END"
