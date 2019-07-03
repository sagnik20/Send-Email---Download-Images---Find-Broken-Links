from selenium import webdriver
import validators
import time
import send_email
import os
import json
from urllib.request import *


os.environ["PATH"] += os.pathsep + os.getcwd()
download_path = "C:/Users/Sagnik Chatterjee/Desktop/abc/"


while (True):

    choice = input("Enter :\n 1. To send an email \n 2. To list out broken urls \n 3. To download images \n Enter your choice \n")

    if (choice == "1"):
        sub = input("Enter your Subject : \t")
        msg = input("Enter your Message : \t")
        reciever = input("Enter recievers email: ")
        send_email.email(sub,msg,reciever)



    elif (choice == "2"):
        broken = []
        url = input("Enter the desired URL :")
        driver = webdriver.Firefox()
        driver.get(url)
        time.sleep(3)
        list_links = driver.find_elements_by_tag_name('a')
        for i in list_links:
            url1 = str(i.get_attribute('href'))
            if validators.url(url1) == False:
                broken.append(url1)
        if broken == []:
            print("All links are OK.")
        for x in broken:
            print(x)
        driver.quit()


    elif (choice == "3"):
        image_count, downloaded_img_count = 0, 0
        searchtext = input("Enter the keyword you want to search for : ")
        extensions = {"jpg", "jpeg", "png"}
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
        driver = webdriver.Firefox()
        driver.get("https://www.google.co.in/search?q="+searchtext+"&source=lnms&tbm=isch")
        if not os.path.exists(download_path + searchtext.replace(" ", "_")):
            os.makedirs(download_path + searchtext.replace(" ", "_"))
        imges = driver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')
        for img in imges:
            img_url = json.loads(img.get_attribute('innerHTML'))["ou"]
            img_type = json.loads(img.get_attribute('innerHTML'))["ity"]
            try:
                if img_type not in extensions:
                    img_type = "jpg"
                req = Request(img_url, headers=headers)
                raw_img = urlopen(req).read()
                f = open(download_path + searchtext.replace(" ", "_") + "/" + str(image_count) + "." + img_type, "wb")
                f.write(raw_img)
                f.close
            except Exception as e:
                print("Download failed: {}".format(e))
            image_count+=1
            if image_count == 10:
                break
        driver.quit()


    else:
        print("Sorry wrong input ; Exiting")
        break
