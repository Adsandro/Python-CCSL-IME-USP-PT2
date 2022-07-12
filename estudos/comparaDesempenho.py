from unicodedata import name
import ordenacao
import random
import time

class contaTempo:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)] #Gera uma lista com n numeros
 #Gera valores de 0 a 999
        return lista
    
    def lista_quase_ordenada(self,n):
        lista = [x for x in range(n)] #Gera uma lista ordenada
        lista[n//10] = -600
        return lista
        
        
    def compara (self, n):
        print('=+'*30)
        print('Compara lista aleatória:')
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:] #Clona a lista

        o = ordenacao.ordenador()
        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print('Tempo de teste da bolha:', depois - antes)
        
        o = ordenacao.ordenador()
        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print('Tempo de teste da seleção direta:', depois - antes)
        print('=+'*30)

    
    
        print('=+'*30)
        print('Compara lista quase ordenada:')
        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]
        
        o = ordenacao.ordenador()
        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print('Tempo de teste de bolha:', depois-antes)

        o = ordenacao.ordenador()
        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print('Tempo de teste de seleção direta:', depois-antes)
        print('=+'*30)

        
        
c = contaTempo()
c.compara(1000)

