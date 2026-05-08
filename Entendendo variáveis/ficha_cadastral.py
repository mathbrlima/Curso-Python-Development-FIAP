#NOME
#PESO
#ALTURA
#IDADE
#TEM PESO MINÍMO PARA DOAR
#TEM IDADE MÍNIMA PARA DOAR
print("Cadastro de doadores de sangue")
nome = input("Por favor, informe seu nome completo: ")
peso = float(input("Por favor, informe seu peso em Kg: "))
altura = int(input("Por favor, informe sua altura em cm: "))
ano_nacimento = int(input("Por favor, informe seu ano de nacimento: "))

idade = 2026 - ano_nacimento
tem_peso_minimo = peso > 50
tem_idade_minima = idade >= 18

texto_saida = (f"\tNome: {nome}\n\tPeso: {peso} kg\n\tAltura: {altura} cm\n\tIdade: {idade} anos\n\tTem peso mínimo para doar: {tem_peso_minimo}\n\tIdade mínima para doar: {tem_idade_minima}")

print(texto_saida)
