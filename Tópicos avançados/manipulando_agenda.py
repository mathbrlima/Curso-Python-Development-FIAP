#tulpla que contém os contatos supotados pelo sistema
contatos_suportados = ("telefone", "email", "endereco")

#Dicionário de exemplo, com alguns dados padrão
agenda = {
    "Pessoa 1":{
        "telefone":["11 1234-5678"],
        "email":["pessoa@email.com", "email@profissional.com"],
        "endereco":["Rua 123"]
    },
    "Pessoa 2":{
        "telefone":["11 9874-5678"],
        "email":["pessoa2@email.com", "pessoa2@profissional.com"],
        "endereco":["Rua 345"]
    }
}

def contador_para_texto(nome_contato:str, **formas_contato):
    formato_texto = (f"{nome_contato}")
    for meio_contato, contato in formas_contato.items():
        formato_texto = (f"{formato_texto}\n{meio_contato.upper()}")
        contador_formas = 1
        for valor in contato:
            formato_texto = (f"{formato_texto}\n\t{contador_formas} - {valor}")
            contador_formas = contador_formas + 1

    return formato_texto

#Função de visualização da agenda completa
def agenda_para_texto(**agenda_completa):
    formato_texto = ""
    for nome_contato, formas_contato in agenda_completa.items():
        formato_texto = f"{formato_texto} {contador_para_texto(nome_contato, **formas_contato)}\n"
        formato_texto = f"{formato_texto}---------------------------\n"
    return formato_texto

print(C(**agenda))

#Função para alterar o nome do contato
def altera_nome_contato(agenda_original:dict, nome_original:str, nome_atualizado:str):
    """Recebe a agenda original em forma de dicionário, o nome_original e o nome_atualizado em forma de string
    Busca o nome original no dicionário e retorna False se não encontrar.
    Retorna True se encontrar o nome original no dicionário e fizer a exclusão do contato antigo e inclusão do novo"""
    if nome_atualizado in agenda_original.keys():
        copia_contato = agenda_original[nome_original].copy()
        agenda_original.pop(nome_original)
        agenda_original[nome_atualizado] = copia_contato
        return True
    return False

altera_nome_contato(agenda, "Pessoa 2", "Super Pessoa")
print(altera_nome_contato(**agenda))