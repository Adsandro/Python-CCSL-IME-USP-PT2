def acha_elemento(lista, x):
    for i in range(len(lista)):
        if lista[i] == x:
            return True
    return False


lista = [1, 2, 3, 4]
x = 0
print(acha_elemento(lista, x))