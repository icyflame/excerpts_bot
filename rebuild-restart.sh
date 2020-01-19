#!/usr/bin/env sh

docker build . -t excerpts:latest &&
    docker container stop excerpts &&
    docker container rm excerpts &&
    docker run -d --name excerpts excerpts:latest
