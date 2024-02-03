valor_casa = float(input('Valor da casa: '))

salario = float(input('Salário: '))

tempo = int(input('Quantidade de anos: '))

prestacao = valor_casa / (tempo * 12)

if prestacao < salario*0.3:
    print(f'Empréstimo liberado. Prestação: {prestacao:.2f}')

else:
    print(f'Empréstimo negado. Prestação maior que 30% do salário.')