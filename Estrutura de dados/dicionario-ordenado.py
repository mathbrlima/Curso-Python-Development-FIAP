#importação do OrderedDict
from collections import OrderedDict
#criação
dicionario_ordenado = OrderedDict()
print(dicionario_ordenado)
#Adicionando chaves e valores
dicionario_ordenado["NOME"] = "Iphone"
dicionario_ordenado["MARCA"] = "Apple"
dicionario_ordenado["MODELO"] = "14 Pro Max"
#percorrendo para verificar a ordem
for chave, valor in dicionario_ordenado.items():
    print(f"{chave} -- {valor}")

#Alterando um item
dicionario_ordenado["MARCA"] = "Maçã"
print()
#percorrendo para verificar a ordem
for chave, valor in dicionario_ordenado.items():
    print(f"{chave} -- {valor}")

#removendo um item
dicionario_ordenado.pop("MARCA")
print()
#percorrendo para verificar a ordem
for chave, valor in dicionario_ordenado.items():
    print(f"{chave} -- {valor}")

#reinserindo um item neste dicionário
dicionario_ordenado["MARCA"] = "Apple"
print()
#percorrendo para verificar a ordem
for chave, valor in dicionario_ordenado.items():
    print(f"{chave} -- {valor}")
