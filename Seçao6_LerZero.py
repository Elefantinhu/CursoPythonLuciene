soma = 0
lidos = 0
valor = int(input("Digite um valor: "))

while valor != 0:
    soma = soma + valor
    lidos = lidos + 1
    valor = int(input("Digite um valor: "))

print("Foram lidos", lidos , "numeros")
print("A soma dos numeros lidos é ", soma)
    