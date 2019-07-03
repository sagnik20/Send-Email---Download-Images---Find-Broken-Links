from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import send_email
import config
while (True):

    choice = input("Enter :\n 1. To send an email \n 2. To list out broken urls \n 3. To download images \n Enter your choice \n")
    #print (choice==1)
    if (choice == "1"):
        sub = input("Enter your Subject : \t")
        msg = input("Enter your Message : \t")
        reciever = input("Enter recievers email: ")
        send_email.email(sub,msg,reciever,config.PASSWORD)
        #driver = webdriver.Firefox()
        #driver.get("")


    elif (choice == "2"):
        driver = webdriver.Firefox()
        driver.get("")

    elif (choice == "3"):
        driver = webdriver.Firefox()
        driver.get("")

    else: break
