salario = float(input('Qual o salário do
funcionário? R$'))
aum = float(input('Digite um aumento: '))
novo = salario+(salario * aum / 100)
print('Um funcionário que ganhava R${:.2f} , com
{}% de aumento passa a receber
R${:.2f}'.format(salario, aum, novo))