with open("arquivo_texto.txt", mode="r", encoding="UTF-8") as arquivo:
    conteudo = arquivo.read()
    #conteudo = arquivo.readline()
    #conteudo = arquivo.readlines()
    #conteudo = arquivo.read().splitlines()

print(conteudo)