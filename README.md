# Excerpts Bot - Email

> A bot to send you an email daily that contains a randomly selected highlight
> from the books you have read

Currently, reads highlights from Kindle notebooks (CSV files) and sends email
via Sendgrid.

## Original

This was originally [Nishant Nikhil](https://twitter.com/nishantiam)'s idea.

His [repository](https://github.com/nishnik/excerpts_bot) has code to post the
randomly chosen highlight on Twitter every 12 hours.

## Environment Variables

Check the .env.template file

## Usage

Running the `tweebot.py` script with the required environment variables will
send a single email. You can use cron to make this a periodic email.

```sh
* 10 * * * python3 /media/username/code/excerpts_bot/tweebot.py
```

## License

Code licensed under MIT

Copyright (C) 2018  Siddharth Kannan <mail@siddharthkannan.in>
