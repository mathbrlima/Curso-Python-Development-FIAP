op = 0
ficha = {}
while op != 4:
    print("\nFICHA CADASTRAL")
    print("1 - Incluir informações na ficha")
    print("2 - Reculperar informações da ficha")
    print("3 - Exibir ficha completa")
    print("4 - Sair")
    op = int(input("Informe a opção desejada: "))

    if op == 1:
        #inserir dados na ficha
        chave = input("Informe o campo que deseja cadastrar na ficha: ")
        valor = input("Informe o dado que deseja cadastrar neste campo: ")
        #ficha[chave] = valor
        ficha.update({chave:valor})#adicionar ou atualizar valores dentro do dicionário

    elif op == 2:
        #recuperar dados da ficha
        print(f"Os campos disponíveis na ficha são {ficha.keys()}")
        chave = input("Informe qual campo deseja exibir: ")
        #print(ficha.get[chave])
        if chave in ficha.keys():
            print(f"O campo {chave} contém o dado {ficha.get(chave)}")
        else:
            print("Você digitou um campo inexistente.")

    elif op == 3:
        #exibir ficha completa
        print("FICHA CADASTRAL")
        for campo, dado in ficha.items():
            print(f"{campo.upper()} --> {dado}")
    elif op == 4:
        print("Saindo do sistema de ficha cadastral")
        break
    else:
        print("Por favor, escolha uma opção válida")