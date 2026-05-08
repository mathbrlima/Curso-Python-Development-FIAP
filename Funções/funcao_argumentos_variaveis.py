def exibe_promocao(*clientes):# * em parâmetros de função → permite que a função aceite vários argumentos posicionais.
    for cliente in clientes:
        print(f"Olá {cliente}!\nQueremos te avisar que a nova X-WING está em promoção!")
lista_clientes = ["Luke", "Princesa Leia", "Mestre Yoda"]
exibe_promocao(*lista_clientes)
#exibe_promocao("Princesa Leia")
#exibe_promocao("Mestre Yoda")