num1 = int(input('Valor 1: '))
num2 = int(input('Valor 2: '))
print('Informe qual operação deseja realizar:')
operacao = input('(+) adição | (-) subtração | (*) multiplicação '
'(\) divisão \n')

if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(num1 - num2)
elif operacao == '*':
    print(num1 * num2)
elif operacao == '/':
    print(num1 / num2)
else:
    print('Operação inválida!')