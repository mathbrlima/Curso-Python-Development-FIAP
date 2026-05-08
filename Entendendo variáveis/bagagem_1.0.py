print("Uma companhia aérea permite que seus clientes do tipo premium despachem bagagens de até 32Kg sem nenhum custo adicional, enquanto os clientes do \ntipo gold podem levar malas de até 28Kg sem nenhum custo adicional e todos os demais devem pagar por qualquer bagagem despachada.")

tipo_cliente = input("Por favor informe o tipo do cliente: PREMIUM, GOLD ou REGULAR: ")
peso_bagagem = float(input("Por favor informe o peso do bagagem que o cliente deseja despachar: "))

if tipo_cliente == "PREMIUM":
    #o que acontece se for Premium
    if peso_bagagem <= 32:
        #Exibir mensagem avisando que pode levar a bagagem
        print(f"Cliente {tipo_cliente}, sua bagagem está dentro do limite permitido! \nNão é necessário pagar nenhum valor para despachá-la")
    else:
        peso_excedente = peso_bagagem - 32
        #Exibir mensagem avisando sobre o peso excedente
        print(f"Os clientes {tipo_cliente} têm direito a despacharem bagagens de até 32Kg. A bagagem execede esse peso em {peso_excedente}Kg. \nDirija - se ao balcão de cobrança para realizar o pagamento refente ao peso adicional.")
else:
    if tipo_cliente == "GOLD":
        #o que acontece se for Gold
        if peso_bagagem <= 28:
            #Exibir mensagem avisando que pode levar a bagagem
            print(f"Cliente {tipo_cliente}, sua bagagem está dentro do limite permitido! \nNão é necessário pagar nenhum valor para despachá-la")
        else:
            peso_excedente = peso_bagagem - 28
            #Exibir mensagem avisando sobre o excedente
            print(f"Os clientes {tipo_cliente} têm direito a despacharem bagagens de até 28Kg. a bagagem atual excede este peso em {peso_excedente}Kg. \nDirija-se ao balcão de cobrança para realizar o pagamento referente ao peso adicional.")

    else:
        #o que acontece se for Regular
        print(f"Os clientes {tipo_cliente} não tem direito à bagagem gratuita. \nFavor dirigir-se ao balção de cobrança para realizar o pagamento pela bagagem.")

