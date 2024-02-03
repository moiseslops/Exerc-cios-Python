numero = 7
diferenca = 0
acertou = False
while not acertou:
    palpite = int(input('Tenta advinhar um numero de 1 a 10: '))
    diferenca = palpite - numero
    if diferenca < 0:
        diferenca = diferenca * -1
    if diferenca == 0:
        acertou = True
        print('Você acertou!')
    elif diferenca < 3:
        print('Você errou por pouco')
    elif diferenca >= 3:
        print('Você passou longe')