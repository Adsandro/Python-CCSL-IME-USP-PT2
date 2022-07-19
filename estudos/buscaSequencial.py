class buscador:
    def busca_sequencial (self, seq, x):
        for i in range(len(seq)):
            if seq[i] == x:
                return True
        return False
    def busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista)-1
        while primeiro <= ultimo:
            meio =(primeiro+ ultimo) //2
            if lista[meio] == x:
                return meio
            else: 
                if x < lista[meio]:
                    ultimo = meio - 1
                else: 
                    primeiro = meio + 1
        return -1

lista = [0, 1, 2, 3, 4, 5, 6, 100, 456, 678]   
               
b = buscador()
print(b.busca_binaria(lista, 100))

c = buscador()
print(c.busca_sequencial(lista, 9))