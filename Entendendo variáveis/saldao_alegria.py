#Uma loja oferece pagamentos por boletos bancários ou por cartão de crédito. Os clientes que pagam através de boleto tem direito à 5% de desconto sobre o valor da compra, enquanto os clientes que pagam através de cartão de crédito podem escolher parcelar a compra até 12x
print("Saldão da alegria")
nome = input("Informe o nome do cliente: ")

total_compra = float(input("Informe o valor total da compra do cliente: "))
forma_pagamento = int(input("Selecione a forma de pagamento: 1 - Boleto ou 2 - Cartão "))

if forma_pagamento == 1:
    total_compra_desconto = total_compra * 0.95
    print(f"O total da compra de R${total_compra:.2f} sofreu um desconto pelo pagamento em boleto. O cliente deverá pagar R$ {total_compra_desconto:.2f}.")
else:
    parcelas = int(input("Informe o número de parcelas desejadas: "))
    valor_parcela = total_compra / parcelas
    print(f"O total da compra de R${total_compra:.2f} será pago em {parcelas} parcelas de R${valor_parcela:.2f}.")