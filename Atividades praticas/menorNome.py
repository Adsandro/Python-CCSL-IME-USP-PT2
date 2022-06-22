def menor_nome(nomes):
    tamanho = len(nomes)
    menor = ''
    lista_formatada = []
    for str in nomes:
        lista_formatada.append(str.strip()) # Remove espaços em branco
    menor = lista_formatada[0]
    for str in lista_formatada:
        if len(str) < len(menor): #Se houver um menor na lista, substituira
            menor = str
    return menor.capitalize()
