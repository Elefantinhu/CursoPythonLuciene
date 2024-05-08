i = 0
notas = []

for i in range(4):
    notas.append(int(input("Digite a nota: ")))
    
soma = sum(notas)
print(soma)
media = soma/4

for nota in notas:
    print("Nota: ", nota)
    
print("Media: ", media)