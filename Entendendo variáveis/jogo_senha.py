resposta = ""
tentativa = 0
while resposta != "python": #!= significa difernete
    resposta = input("Digite a senha secreta: ")
    tentativa = tentativa + 1

print("A senha correta foi digitada")
print(f"Foi preciso usar {tentativa} tentativas para o acerto")