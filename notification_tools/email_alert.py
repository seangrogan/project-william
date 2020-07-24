# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage


def email_alert(message=None):
    # Open the plain text file whose name is in textfile for reading.
    # with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(message)

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = f'test'
    msg['From'] = "sean.grogan@gmail.com"
    msg['To'] = "sean.grogan+ALERT@gmail.com"

    # Send the message via our own SMTP server.
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()
    return 0


if __name__ == '__main__':
    email_alert("T E S T")