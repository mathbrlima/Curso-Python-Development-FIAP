lista = [12, 15.5, "texto"]
print(type(lista))

#inserindo novos elementos
lista.append("Teste de inserção")
#mostrando a lista inteiro
print(lista)
#mostrando elemento pelo índice
print(lista[0])#primeiro para o último
print(lista[-4])#último para o primeiro
print(lista[0:3])#exibira o primero elemento do indice colocado até os segundo elemento -1 (me exiba os elementos que estão no índice 0 até o indice 3-1)

#exibindo com loop
for valor in lista:
    print(valor)
#removendo
lista.pop()
print(lista)
lista.remove(12)#remove o índice especificado
print(lista)

#tamanho da lista
print(len(lista))#quantidade de elementos na lista