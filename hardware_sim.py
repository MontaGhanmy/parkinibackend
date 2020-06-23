#!/usr/bin/python3
import requests
import sys

data = {"matricule": "", "id": ""}
ENPOINT = "http://127.0.0.1:8000/notification/"
try:
    data["matricule"] = str(input("Veuillez saisir votre plaque d'immatriculation:"))
except e:
    print("Vous devez saisir votre plaque d'immatriculation!")

data["id"] = sys.argv[1]

response = requests.post(url=ENPOINT, json=data)

print(response)