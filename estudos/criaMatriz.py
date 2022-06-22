def criaMatriz(num_linha, num_Coluna, valor):
    matriz = []
    for i in range(num_linha):
        linha = []
        for j in range(num_Coluna):
            linha.append(valor)
        matriz.append(linha)
    return matriz

if __name__ == '__main__':
    num_Linha = int(input('Informe o numero de linhas: '))
    num_Coluna = int(input('Informe o numero de colunas: '))
    valor = int(input('Informe o valor que deve representar: '))
    print(criaMatriz(num_Linha, num_Coluna, valor))