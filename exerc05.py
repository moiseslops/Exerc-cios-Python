num_1 = int(input('Digite o primeiro valor: '))
num_2 = int(input('Digite o segundo valor: '))
if num_1 == num_2:
    print('Os dois números digitados são iguais ')
elif num_1 > num_2:
    print('O seu primeiro número: {} é maior que o segundo número: {}'.format(num_1, num_2))
elif num_2 > num_1:
    print('O seu segundo numero: {} é maior que o primeiro número: {}'.format(num_2, num_1))