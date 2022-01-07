import datetime
import pandas as pd
import numpy as np
import smtplib
import ssl
from email.mime.text import MIMEText as MT 
from email.mime.multipart import MIMEMultipart as MM 
from sender import Sender 

# Load the birthday list data
df = pd.read_excel('Birthdays.xlsx')
print(df)

def send_email(subject, birthday_receiver, name):
    receiver = birthday_receiver
    sender = Sender()
    sender_email = sender.getEmail()
    sender_password = sender.getPassword()

    # Create a MIMEMultipart Object
    msg = MM()
    msg['Subject'] = subject + ' ' + str(name) + '!'

    # Create the HTML for the message
    HTML = """
    <html>
        <body>
            <h1>Happy Birthday ! </h1>
            <img src="https://top10tphcm.com/wp-content/uploads/2018/11/banhkem1.jpg" alt ="Image" width="640" height="360">
            <h2>
                <p>Hello,<br>
                I hope you have a wonderful day today ! <br><br>
                From;<br>
                Your Friend
                </p>
            </h2>
        </body>
    </html>
    """

    # Create a html MIMEText object
    MTObj = MT(HTML, "html")

    # Attach the MIMEText object into the message container
    msg.attach(MTObj)

    # Create a secure connection with the server and send the email
    SSL_context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=SSL_context)
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver, msg.as_string())

# Get time
today = datetime.date.today()
year = today.year

for i in range(0, len(df)):
    month = df['Birth_month'][i]
    day = df['Birth_day'][i]
    name = df['Name'][i]
    email = df['Email'][i]
    birthdate = datetime.date(year, month, day)

    if birthdate == today:
        send_email('Happy Birthday', email, name)
        print('Sent mail')
    else:
        print('Did not send mail')