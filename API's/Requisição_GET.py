import requests

resp = requests.get("https://viacep.com.br/ws/01001000/json/", timeout=10)
resp.raise_for_status()                # vira exceção se for 4xx/5xx
dados = resp.json()
print(dados["logradouro"])             # Praça da Sé