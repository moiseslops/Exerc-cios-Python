consumo = float(input('Informe o total de água consumida (m3): '))
conta = 0.0
if consumo <= 30:
    conta = consumo*5
elif consumo <= 50:
    conta = consumo*7
elif consumo <= 100:
    conta = consumo*9
else:
    conta = consumo*10
print(f'Conta: R$ {conta}')