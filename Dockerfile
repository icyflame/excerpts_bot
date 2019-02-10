FROM python:3-alpine

WORKDIR /
COPY . ./

RUN ["pip3", "install", "-r", "requirements.txt"]

COPY run-tweebot /etc/periodic/daily
# COPY run-tweebot /etc/periodic/15min

CMD ["./run_cron.sh"]
