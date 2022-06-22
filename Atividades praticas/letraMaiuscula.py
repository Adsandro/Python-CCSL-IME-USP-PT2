def maiusculas(frase):
    letras = '' #Lista e str para armazenar
    lista = []

    for c in frase: 
        if ord(c) >= 65 and ord(c) <= 91:
            lista.append(c)    
    letras = ''.join(lista)
    return letras

#https://pt.wikipedia.org/wiki/ASCII