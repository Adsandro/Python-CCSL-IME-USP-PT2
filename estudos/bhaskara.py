import math

class bhaskara:
    def delta(self, A, B, C):
        return B ** 2 - 4 * A * C

    def bhaskara (self):
        valor_A = float(input('Digite o valor de A: '))
        valor_B = float(input('Digite o valor de B: '))
        valor_C = float(input('Digite o valor de C: '))
        print(self.calcula_raizes(valor_A, valor_B, valor_C))

    def calcula_raizes(self, A, B, C):
        d = self.delta(A, B, C)
        if d ==0:
            raiz1 = (-B + math.sqrt(d)) / (2*A)
            return 1, raiz1
        else:
            if d < 0:
                return 0
            else:
                raiz1 = (-B + math.sqrt(d)) / (2*A)
                raiz2 = (-B - math.sqrt(d) / (2*A))
                return 2, raiz1, raiz2
        
b = bhaskara()
b.bhaskara()