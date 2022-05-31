matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for l in range(0,3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f"Digite o valor de [{l},{c}]:"))
print("-="*30)
for l in range(0,3):
    for c in range(0, 3):
        print(f"[{matriz[f][c]}]", end="")
    print() #realiza a quebra de linha quando acaba a coluna 
    

