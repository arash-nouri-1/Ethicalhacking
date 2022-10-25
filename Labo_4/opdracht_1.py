from bs4 import BeautifulSoup
import os
import requests
import sys

URL = sys.argv[1]
reponse = requests.get(URL)
admin_page = requests.get(URL + "/admin")

if reponse.ok:
    home_page = BeautifulSoup(reponse.text, "lxml")
    admin_page = BeautifulSoup(admin_page.text, "lxml")
    csrf = str(home_page.find("input", {"name": "csrfmiddlewaretoken"}))
    title = str(admin_page.find("title"))

    if "csrfmiddlewaretoken" in csrf or "Django" in title:
        #        print(csrf + "\n" + title)
        print("Het is EEN django website!")
    else:
        print("Het is GEEN django website!")
else:
    print("Error: " + str(reponse.status_code))
