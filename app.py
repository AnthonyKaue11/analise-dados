import requests

cep = input("Digite o seu cep:")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url)
resposta = dados.json()

print(f"Você mora na rua {resposta["logradouro"]}, no bairro {resposta["bairro"]}")