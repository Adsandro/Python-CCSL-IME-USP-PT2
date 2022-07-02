class Triangulo:
    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        if self.a == self.b == self.c:
            return ('equilátero')
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return ('isósceles')
        else:
            return ('escaleno')
            
def main ():
    
    a = input('Informe a ')
    b = input('Informe b ')
    c = input('Informe c ')    
    t = Triangulo(a, b, c)
    print(t.perimetro())
    print(t.tipo_lado())
     
main()
