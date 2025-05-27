import requests
import os

site = os.getenv("INPUT_SITE")
resposta = requests.get(site)

print(resposta.status_code)
