from ast import main
import requests


def get_website_urls(URL, file):
    for path in file:
        full_url = f"{URL}/{path}"
        full_url = full_url.rstrip() + "/"
        response = requests.get(full_url)
        if response.status_code == 200:
            with open("output.txt", "a") as f:
                f.write(full_url)


def main():
    URL = "http://localhost:8000"

    with open("output.txt", "w") as f:
        pass

    with open("all.txt", "r") as file:
        get_website_urls(URL, file)


if __name__ == "__main__":
    main()
