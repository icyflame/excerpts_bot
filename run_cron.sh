#!/usr/bin/env sh

set -xe

touch /var/log/cron.log
crond && tail -f /var/log/cron.log
