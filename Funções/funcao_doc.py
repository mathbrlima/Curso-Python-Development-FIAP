def somar(a:float, b:float):
    """Função que realiza a soma entre dois valores e retorna um resultado.
     Dois argumentos, a e b, são obrigatórios e são do tipo float."""
    return a + b


print(somar.__doc__)
print(help(somar))


#Docstring (__doc__)
#É um texto de documentação que você escreve dentro da função entre três aspas
# """ ... """.
#Serve para explicar o que a função faz, quais argumentos ela recebe e o que retorna.
#Você pode acessar esse texto usando o atributo __doc__ da função.

#help()
#É uma função do Python que mostra informações detalhadas sobre a função, classe ou módulo, incluindo a docstring.
#Serve como uma “ajuda interativa”, muito útil quando você quer revisar ou aprender como usar algo.