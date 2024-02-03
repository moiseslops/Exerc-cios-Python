numero = 7
diferenca = 0
palpite = int(input('Tenta adivinhar um número de 1 a 10:'))
diferenca = palpite - numero
if diferenca < 0:
    diferenca = diferenca * -1
if diferenca == 0:
    print('Você acertou!')
elif diferenca < 3:
    print('Você errou por pouco')
elif diferenca >= 3:
    print('Você passou longe')