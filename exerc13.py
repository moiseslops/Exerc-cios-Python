velocidade = int(input('Qual a velocidade? '))
limite = 80
if velocidade > limite:
    multa = (velocidade - limite) * 50
    print(f'O condutor foi multado em R$ {multa},00')