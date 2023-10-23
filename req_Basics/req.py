#!/usr/bin/python3
import requests
import webbrowser
session = requests.Session()
url = "https://tryhackme.com/login"
#login=hello&passwd=hello123&submit_login=login
data = {"login":"testuser",
        "passwd":"testpass",
        "submit_login":"login"}
session.post(url,data=data)
r = session.get('https://tryhackme.com/')
file = open('file.html','wb')
file.write(r.content)
file.close()

webbrowser.open('file.html')
