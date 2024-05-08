nome1 = str(input("Digite o Nome da Pessoa 1: "))
idade1 = int(input("Digite a Idade da Pessoa 1: "))
nome2 = str(input("Digite a Nome da Pessoa 2: "))
idade2 = int(input("Digite a Idade da Pessoa 2: "))


if idade1 > idade2 :
    print(nome1 + " é mais velho")
elif idade1 == idade2 :
    print(nome1 + " e " + nome2 + " tem a mesma idade")
else:
    print(nome2 + " é mais velho")


