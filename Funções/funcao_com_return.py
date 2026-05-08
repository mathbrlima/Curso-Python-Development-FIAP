def soma(a, b):
    resultado = a + b
    return resultado#return permite que uma função entregue dados para o resto do programa, para que você possa usar, armazenar ou processar esses dados depois.

valor1 = int(input("Digite o primeiro valor que deseja somar: "))
valor2 = int(input("Digite o segundo valor que deseja somar: "))

resposta = soma(valor1, valor2)
print(f"A resposta é {resposta}")
print(f"A resposta é {soma(valor1, valor2)}")

#Sem return → a função só faz algo dentro dela, como imprimir na tela, mas você não pode guardar ou usar o valor.
#Com return → a função gera um dado e devolve para você, que pode ser armazenado em uma variável, usado em cálculos ou passado para outra função.