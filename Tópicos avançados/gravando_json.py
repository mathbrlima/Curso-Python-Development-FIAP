#json é um formato de texto usado para representar e trocar dados entre sistemas.
import json
dicionario = {
    "nome": "Python",
    "missão": "Ser incrível!"

}

conteudo = json.dumps(dicionario, ensure_ascii=False, indent=4)
with open("arquivo.json", mode="w", encoding="UTF-8") as arquivo:
    arquivo.write(conteudo)

print("Arquivo gerado corretamente")

#dumps → transforma dados em texto JSON
#ensure_ascii=False → mantém acentos
#indent=4 → organiza visualmente