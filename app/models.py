# app/services.py

from app import db
from app.models import ExternalData
import requests

def fetch_and_store_external_data():
    url = "https://api.external.com/data"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for item in data:
            # Assuming ExternalData is a model class representing your data schema
            record = ExternalData(name=item['name'], value=item['value'])
            db.session.add(record)
        db.session.commit()
