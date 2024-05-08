i = 0
idades = []

for i in range(20):
    idades.append(int(input("Digite a idade: ")))


maior = max(idades)
menor = min(idades)

print("Maior idade é: ", maior)
print("Menor idade é: ", menor)