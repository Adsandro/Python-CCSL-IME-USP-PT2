# '''coleção sequencial de caracteres'''

time = "palmeiras"
print(time[0])
print(time[1])
print(time[2])
print(time[3])

print(time.upper()) #Coloca os caracretes em maiusculo
print(time.lower())

print("marina te amo".capitalize()) #Primeira letra maiuscula

print("   adsandroxerd@gmail.com   ".strip()) #Remove estaços em branco

print("Anticonstitucionalissimamente".count("t")) #Contar quantidade de tais letras

print("eu torço para o São Paulo".replace("São Paulo", "Palmeiras")) #Troca de palavras

print("marina te amo".capitalize().center(80)) #centraliza o texto

texto = "Lorem ipsum dolor sit amet."
print(texto.find("d")) #Encontrar a primeira vez que tal letra aparece

print(len(texto)) #Tamanho do texto

fruta = "amora"
print(fruta[0:4]) #Corta o texto