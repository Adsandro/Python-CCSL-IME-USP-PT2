from inspect import BoundArguments


class animal:
    pass

Macaco = animal()

Macaco.Idade = 10
Macaco.Cor = 'Marrom'
Macaco.Rabo = True


Girafa = animal()

Girafa.Pescoco = 20
Girafa.Albina = False
Girafa.Idade = 30
Girafa.Nome = 'Botas'


Botas = Girafa #Duas variaveis para um objeto
Botas.Idade += 10

print(Botas.Nome)
print(Botas.Idade)