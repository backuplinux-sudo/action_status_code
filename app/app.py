import requests
import os

site = os.getenv("INPUT_SITE")
resposta = requests.get(site)

print(f"Site: {site} | Código: {resposta.status_code}")
