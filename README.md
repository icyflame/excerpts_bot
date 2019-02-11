# Excerpts Bot - Email

> A bot to send you an email daily that contains a randomly selected highlight
> from the books you have read

Currently, reads highlights from Kindle notebooks (CSV files) and sends email
via Sendgrid. Original repository [here][2].

## TOC

- [Original](#original)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
    - [Local Setup](#local-setup)
        - [Setup](#setup)
        - [Using Cron](#using-cron)
    - [Dockerized Setup](#dockerized-setup)

## Original

This was originally [Nishant Nikhil](https://twitter.com/nishantiam)'s idea.

His [repository][2] has code to post the
randomly chosen highlight on Twitter every 12 hours.

## Environment Variables

Check the .env.template file

## Usage

### Local setup

#### Setup

```sh
$ git clone https://github.com/icyflame/excerpts_bot.git
$ cd excerpts_bot
$ mkdir -p dir_to_lookup
$ cp .env.template .env
```

You can put your Kindle notebooks into `/dir_to_lookup`. And see the `.env`
file for the environment variables that are required for this script to run.
Once these have been completed, you can run the script using:

```sh
$ python3 tweebot.py
```

#### Using Cron

Running the `tweebot.py` script with the required environment variables will
send a single email. You can use cron to make this a periodic email.

```sh
* 10 * * * python3 /media/username/code/excerpts_bot/tweebot.py
```

### Dockerized setup

1. Get an instance on your preferred cloud provider
    1. You can use the cheapest instance the provider offers
    1. This is only a cron that is going to run once and doesn't need any
       significant RAM or Hard Disk
    1. If you already have an app instance, you can run this together with that
       as well (Thanks, [Docker][1]!)
1. SSH into your instance
1. Follow the steps in `Local Setup > Setup`
1. Build the docker container:

    ```sh
    docker build . -t excerpts:latest
    ```

1. Run the docker container:

    ```sh
    docker run --name excerpts -d excerpts:latest
    ```

***

By default, the script is set to run once a while. The base docker image is
alpine and alpine has the convenient `/etc/periodic/daily` which runs the script
once every day at 2 am.

## License

Code licensed under MIT

Copyright (C) 2018  Siddharth Kannan <mail@siddharthkannan.in>

[1]: https://docs.docker.com/
[2]: https://github.com/nishnik/excerpts_bot
