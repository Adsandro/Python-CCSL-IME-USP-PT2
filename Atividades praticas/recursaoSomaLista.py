def soma_lista(lista):
    if len(lista)== 1:
        return lista[0]
    else:
        soma = 0
        for i in range(len(lista)):
            soma +=lista[i]
        return soma