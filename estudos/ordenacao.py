class Ordenador:
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