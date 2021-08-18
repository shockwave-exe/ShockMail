import pandas as pd
import stdiomask as mask
import getpass
import smtplib

SenderAddress = input("Enter your email address")
password = mask.getpass()

e = pd.read_excel("emailss.xlsx")
emails = e['emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
msg = input("ENTER BODY OF THE MAIL : ")
subject = input("ENTER SUBJECT FOR THE MAIL : ")
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail(SenderAddress, email, body)
    print("email sent to : ",email)
server.quit()