#Para(for) variável(contadora) dentro de(in)
for contadora in range(10, 100, 2): #range é usado para gerar uma sequência de números automaticamente.
    print(contadora)
    if contadora == 20:
        break #usado para parar a programação

numero = int(input("Por favor, informe o número do qual deseja o fatorial: "))
fat = numero

for valor in range(1, numero, 1):
    fat = fat * valor

print(f"O fatorial para o valor informado foi {fat}")

