import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the SMTP server details
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # Port for TLS/STARTTLS

# Your email credentials
sender_email = 'ijespinoza00@gmail.com'
sender_password = 'pqjf mkps zcub tjhr'

# Recipient email address
recipient_email = 'ijespinoza000@gmail.com'

# Create a message object
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = 'Test Email from Python'

# Add body to email
body = 'Hello, this is a test email sent from Python!'
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Enable encryption
server.login(sender_email, sender_password)

# Send the email
server.sendmail(sender_email, recipient_email, message.as_string())

# Quit the server
server.quit()

print('Email sent successfully!')
