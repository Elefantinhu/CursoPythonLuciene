nome = str(input("Digite o nome do Funcionario:"))
salariofixo = float(input("Digite o Salario Fixo do Funcionario:"))
vendas = float(input("Digite as Vendas do Funcionario:"))

aumento = (vendas*15)/100
total = aumento + salariofixo

print(f'TOTAL = R$  {total:.2f}')