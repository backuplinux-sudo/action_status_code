import requests
import os

site = os.getenv("INPUT_SITE")
resposta = requests.get(site)
os.system(f"echo STATUS_CODE={resposta.status_code} >> $GITHUB_OUTPUT")

