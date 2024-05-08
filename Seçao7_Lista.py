i = 0
lista = []

for i in range(5):
    lista.append(input("Digite um numero: "))

for posicao, elemento in enumerate(lista):
    print("Posiçao: ", posicao, "Numero: ", elemento)