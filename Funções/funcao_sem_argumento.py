def calcular_velociade_media(): #usada para definir uma função, ou seja, um bloco de código reutilizável que realiza uma tarefa específica.

    #Código da nossa função
    velocidade_media = distancia / tempo
    #exibir resultado
    print(f"A velocidade média é {velocidade_media}")


#solicitar distância e tempo
distancia = float(input("Digite a distância percorrida "))
tempo = float(input("Digite o tempo da viagem "))
calcular_velociade_media()