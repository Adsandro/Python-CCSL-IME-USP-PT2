import ordenacao
import random
import time

class contaTempo:
    def lista_aleatoria(self, n):
        lista = [0 for x in range(n)] #Gera uma lista com n numeros
        for i in range(n):
            lista[i] = random.randrange(1000) #Gera valores de 0 a 999
        return lista
    
    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:] #Clona a lista

        o = ordenacao.ordenador()
        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print('Tempo de teste da bolha:', depois - antes)
        
        o = ordenacao.ordenador()
        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print('Tempo de teste da seleção direta:', depois - antes)
    
    
c = contaTempo()
c.compara(5000)