#!/bin/bash

# Schedule this script using crontab
# 10 * * * * bash /home/siddharth/excerpts_bot/keep_container_running.sh

cd /home/siddharth/excerpts_bot

echo "START"
date +"%F %R"

docker container ls | grep -i excerpts > /dev/null
if [[ "$?" != "0" ]];
then
        echo "Restarting container"
        docker container stop excerpts
        docker container rm excerpts
        docker run -d --name excerpts excerpts:latest
else
        echo "Container is running, no need to restart"
fi

date +"%F %R"
echo "END"
