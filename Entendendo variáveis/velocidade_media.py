print("Simulador de computador de bordo")
distancia = float(input("Por favor, informe os quilômetros percorridos: "))
tempo = float(input("Por favor informe quantas horas foram de viagem: "))

velocidade_media = distancia / tempo
#print("A velocidade média é de: {} km/h".format(velocidade_media))
#print(f"A velocidade média é de: {velocidade_media:} km/h")

#print("A velocidade média é de: {:.2f} km/h".format(velocidade_media))
print(f"A velocidade média é de: {velocidade_media:.2f} km/h")

