import json

with open("arquivo.json", mode="r", encoding="UTF-8") as arquivo:
    conteudo = arquivo.read()

contudo_convertido = json.loads(conteudo)

print(contudo_convertido)
print(type(contudo_convertido))