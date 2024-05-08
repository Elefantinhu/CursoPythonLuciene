i = 0
lista = []

for i in range(10):
    lista.append(input("Digite um numero: "))


lista.reverse()
for numero in enumerate(lista):
    print("Posiçao: ", "Numero: ",numero)