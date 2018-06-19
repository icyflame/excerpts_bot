import random
import os
import csv
from datetime import datetime

import sendgrid
from sendgrid.helpers.mail import *

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), verbose=True)

FOLDER_PATH = os.getenv("DIR_WITH_CSV")
TYPE_INDEX = 0
QUOTE_INDEX = 3


def choose_excerpt(file_path, file_type):
    '''
    accepts a file path and the "type" of file it is (i.e Kindle highlights,
    Android text file, etc)

    returns a dictionary with the following keys:
        - quote
        - book
    '''
    if os.path.isfile(file_path):
        if file_type == "kindle_csv":
            with open(file_path, 'r') as csvfile:
                highlights = csv.reader(csvfile, delimiter=',', quotechar='"')

                # convert csv reader object to a list
                highlights = [h for h in highlights]

                book_name = "%s %s" % (highlights[1][0], highlights[2][0])

                highlights = [h for h in highlights \
                        if (len(h) > 1 and h[TYPE_INDEX].startswith("Highlight"))]
                chosen = random.choice(highlights)

                return {
                        "book": book_name,
                        "quote": chosen[QUOTE_INDEX]
                        }
        else:
            return "TYPE NOT SUPPORTED"

def get_quote():
    files = os.listdir(FOLDER_PATH)
    print("Files: ", files)
    files = [f for f in files if f.endswith('.csv')]

    to_open = random.choice(files)

    fname = os.path.join(FOLDER_PATH, to_open)

    return choose_excerpt(fname, "kindle_csv")

def main():
    print("%s" % datetime.now().isoformat())
    print("Getting quote")
    h = get_quote()

    mail_pt_context = '\n'.join([ 
            "Today's Excerpt",
            "",
            "%s" % h['quote'],
            "",
            "from the book %s" % h['book']
        ])

    mail_html_context = ''.join([
                                "<h1>Today's Excerpt</h1>",
                                "<blockquote>%s</blockquote>" % h['quote'],
                                "<p>-- %s</p>" % h['book']
                                ])

    sg = sendgrid.SendGridAPIClient(apikey=os.getenv("SENDGRID_API_KEY"))
    from_email = Email(os.getenv("SENDER_EMAIL"))
    to_email = Email(os.getenv("RECEIVER_EMAIL"))
    subject = "Today's Excerpt"
    content = Content("text/html", mail_html_context)
    mail = Mail(from_email, subject, to_email, content)
    print("Sending email")
    response = sg.client.mail.send.post(request_body=mail.get())

    print("Email sent. Response: ")

    print(response.status_code)
    print(response.body)
    print(response.headers)

if __name__ == '__main__':
    main()
