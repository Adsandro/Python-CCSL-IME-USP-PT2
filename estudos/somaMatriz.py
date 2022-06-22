import criaMatriz

def somaMatriz(A, B):
    numLin = len(A)
    numCol = len(A[0])
    C = criaMatriz.criaMatriz(numLin, numCol, 0)

    for lin in range(numLin):
        for col in range(numCol):
            C[lin][col] = A[lin][col] + B[lin][col]

    return C

if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    print(somaMatriz(A, B))