a, b = 10, 20 
print(a, b)
a, b = b, a
print(a, b)
#trocando os valores entre a e b


#Atribuição aumentada
x = 10
x += x
print(x)
y = 10
y *= 2 
print(y)


#Valor padrão para parametro
def pagamento_semanal(valor_por_hora, num_horas = 40):
    assert valor_por_hora >=0 and num_horas > 0 #Asserção de invariantes
    return valor_por_hora * num_horas
