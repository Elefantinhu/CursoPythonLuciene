nota = 0
lidos = 0
notas = []

notas.append(int(input("Digite a Próxima Nota: ")))
nota = min(notas)

while nota > 0:
    lidos = lidos + 1
    notas.append(int(input("Digite a Próxima Nota: ")))
    nota = min(notas)

notas.remove(min(notas))

print("Foram lidas: ",lidos, "notas")

for posicao, nota in enumerate(notas):
    print("Posiçao: ", posicao, "Nota: ", nota)


notas_inversa = reversed(notas)  
for posicao, nota in enumerate(notas_inversa):
    print("Posição:", posicao, "Nota:", nota)

notas_soma = sum(notas)
print("A soma das notas é: ",notas_soma)
notas_media = notas_soma/lidos
print(f"A media das notas é: {notas_media:.2f}")

notas_acima_media = [nota for nota in notas if nota > 6]
print("As notas acima da média foram: ", notas_acima_media)


