#Dados
#Star Wars - Episódio IV - uma nova esperança, George Lucas, 1977, 775000000.00

#Criação do dicionário
dicionario = {
    #chave      values
    "nome":"Star Wars - Episódio IV - uma nova esperança",
    "diretor":"George Lucas",
    "ano de lançamento":1997,
    "bilheteria":775000000.00
}
#Exibição dicionário completo
print(dicionario)

#Exibição do valor de uma chave
print(dicionario["nome"])

#Inserção de uma nova chave e valor (genêro)
dicionario["genêro"] = "Space Opera"
print(dicionario)

#Função Keys - Mostra as chaves
print(dicionario.keys())
for chave in dicionario.keys():
    print(chave)

#Função Values - Mostra os valores
print(dicionario.values())
for valor in dicionario.values():
    print(valor)

#Função items - Mostra chave + valor juntos
print(dicionario.items())
for chave, valor in dicionario.items():
    print(f"{chave} --> {valor}")

#Função get - buscar (checar se existe) o valor
print(dicionario.get("público"))
print(dicionario.get("nome"))

#Função setdefault - Criar a chave se não existir
dicionario.setdefault("público", 1000)
print(dicionario)
dicionario.setdefault("público", 9000)
print(dicionario)
#quando o setdefault percebe que a chave já existe não altera o valor dela

#resuminho
#keys → chaves
#values → valores
#items → os dois
#get → buscar seguro
#setdefault → cria se não existir