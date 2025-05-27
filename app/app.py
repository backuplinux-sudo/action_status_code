import requests
import os

site = os.getenv("INPUT_SITE")
resposta = requests.get(site)
os.system("echo STATUS_CODE={resposta.status_code} >> $GITHUB_OUTPUT")

