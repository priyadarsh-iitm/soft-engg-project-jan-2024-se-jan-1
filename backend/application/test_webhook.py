import pytest
import requests
import json

def test_webhook():
    data={"message":"¡Bienvenidos al Discurso! Ha habido una actualización i.e Welcome to Discourse !There has been an update"}
    data=json.dumps(data)
    response = requests.post("http://localhost:5000/webhook", data=data, headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert response.json() == {"status": "Message sent successfully"}