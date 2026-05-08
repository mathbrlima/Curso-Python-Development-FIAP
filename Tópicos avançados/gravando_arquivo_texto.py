texto_para_gravar = "Este texto será gravado!"

with open("arquivo_texto.txt", mode="w", encoding="UTF-8") as arquivo:
    arquivo.write(texto_para_gravar)

print("O arquivo foi gravado!")