import json
from apis import authentication
import urllib.request
from urllib.request import urlopen
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_mail(from_email:str, to_emails:tuple, subject:str, html_content:str):
    message = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject=subject,
        html_content=html_content
    )
    try:
        token = authentication.get_token('https://www.apitutor.org/sendgrid/key')
        sg = SendGridAPIClient(token)
        sg.send(message)
        print('Email sent.')
        # response = sg.send(message)
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
    except Exception as e:
        print(e)