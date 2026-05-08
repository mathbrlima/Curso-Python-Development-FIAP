def calcular_velociade_media(distancia:float, tempo:float, unidade_medida = "Km/h"): #usada para definir uma função, ou seja, um bloco de código reutilizável que realiza uma tarefa específica.

    #Código da nossa função
    velocidade_media = distancia / tempo
    #exibir resultado
    print(f"A velocidade média é {velocidade_media}{unidade_medida}")

#solicitar distância e tempo
calcular_velociade_media(200, 3)

calcular_velociade_media()