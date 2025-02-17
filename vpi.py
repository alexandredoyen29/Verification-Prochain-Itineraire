import requests

def get():
    url = "https://prim.iledefrance-mobilites.fr/marketplace/estimated-timetable?LineRef=STIF%3ALine%3A%3AC00680%3A"
    headers = {
        "accept": "application/json",
        "apiKey": "i2Mkal2UiaNMGH9qK5giHc503kxffJIe"
    }

    return requests.get(url, headers = headers).json()