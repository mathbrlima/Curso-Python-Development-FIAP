texto = "Esse texto quebra de linha \naqui. Porém aqui temos uma \ttabulação"
print(texto)

texto = "texto em minúsculas AINDA É texto"
print(texto.capitalize())#corrije a os dois

print(texto.upper())#transorma em MINÚSCULA
print(texto.lower())#transforma em MAÍUSCULA
print(texto.startswith("tex"))#verificar começo
print(texto.endswith("!"))#verificar o final
print(texto.count("m"))#contar quantos tem na frase
print("em" in texto)# encontra se há essa palavra na frase
print(texto.replace("AINDA", "com certeza" ))#substitui palavras