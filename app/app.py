import requests
import os

site = os.getenv("INPUT_SITE")
resposta = requests.get(site)
#os.system(f"echo STATUS_CODE={resposta.status_code} >> $GITHUB_OUTPUT")

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"STATUS_CODE={resposta.status_code}\n")