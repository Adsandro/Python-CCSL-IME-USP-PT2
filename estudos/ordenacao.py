class ordenador:
   def selecao_direta(self,lista):
        fim=len(lista)
        for i in range(fim - 1):
            #Inicialmente,omenor elemento já vistoéoi-ésimo
            posicao_do_minimo = i
            
            for j in range (i+1 ,fim):
               if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
            #Colocaomenor elemento encontrado no início da sub-lista
            #Para isso,troca de lugar os elementos nas posiçõesieposicao_do_minimo
            lista[i],lista[posicao_do_minimo]=lista[posicao_do_minimo],lista[i]
                  
   def bolha_curta(self, lista):
      fim = len(lista)  #Determina o fim da lista
      for i in range(fim -1, 0, -1):
         trocou = False
         for j in range(i):
            if lista[j] > lista[j+1]: 
               lista[j], lista[j+1] = lista[j+1], lista[j] #Troca os valores comparados de lugar
               trocou = True
         if not trocou: #Caso não tenha realizado a troca, o programa ira finalizar
            return

               

if __name__ == '__main__':
   o = ordenador()
   lista = [85, 96, 19, 8, 54, 99, 76, 94, 95]

   o.bolha_curta(lista)
   print(lista)
