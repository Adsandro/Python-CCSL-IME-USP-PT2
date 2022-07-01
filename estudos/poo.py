class carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        
carroAdsandro = carro('fuca', 2000,'amarelo')

print(carroAdsandro.ano, carroAdsandro.modelo, carroAdsandro.cor)
