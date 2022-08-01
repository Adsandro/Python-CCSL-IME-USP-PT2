def busca_binaria(lista, elemento, min=0, max= None): #Caso não seja informadoo nada na chamada da função, esses serão os elemento min e max
    if max == None:
        max = len(lista)-1

    if max < min:
        return False #Caso o elemento não esteja na lista
    else:
        meio = (min + max) //2

    
    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, min, meio -1)
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio+1, max)
    else:
        return meio
    

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16]
print(busca_binaria(lista, 16))