# importing smtplib module : It is the actual sending function liberary
import smtplib
from email.message import EmailMessage



file = open("msg_file.txt" , "a")  # creating a empty msg text_file or if its already created then we will appending the data into it
# Writing massage to the above opened file
file.write(" hii guy's how are you. i hope you all are filne and shine.. ")
file.close()
# creating a plain txt msg and set it to variable msg
msg = EmailMessage()
file = open("msg_file.txt")
# setting up the above file msg to main content of the mail
msg.set_content(file.read())

msg['Subject']=f'The Content of {file}'
msg['From']= "bkkanhaya@gmail.com"
msg['To']= "techamanjeet1@gmail.com"

# now setting up the msg file to send from our own localhost
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()