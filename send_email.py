import smtplib
import config


def email(subject, msg, reciever, password = config.PASSWORD):

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL, password)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL, reciever, message)
        server.quit()
        print("Success: Email sent!")

        print("Email failed to send.")

'''
subject = "Test subject"
msg = "Hello there, how are you today?"
username= config.EMAIL_ADDRESS
password= config.PASSWORD


email(username, password, subject, msg)
'''