import requests
import json


def get_data():
    res = requests.get()
    if res.status_code == 200:
        print("Connection working fine")
    else:
        print("Error is connection")


get_data("https://api.restful-api.dev/objects")
