#app/api.py

import requests

def get_external_data():
    url = "https://api.external.com/data"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
