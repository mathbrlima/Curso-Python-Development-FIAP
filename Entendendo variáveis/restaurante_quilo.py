from types import prepare_class

print("Restaurante por quilo")

preco_quilo = 63#exemplo de preço escolhido por estabelecimento
peso_prato = float(input("Informe o valor do peso do prato do cliente (em Kg): "))

preco_prato = preco_quilo * peso_prato

print(f"O preço do prato é de R${preco_prato:.2f}")

if peso_prato > 1:
    print("Como o peso do cliente ultrapassou 1Kg, ele deve pagar um valor fixo de R$80,00")