import requests

site = "https://pudim.com.br"
resposta = requests.get(site)

print(resposta.status_code)
