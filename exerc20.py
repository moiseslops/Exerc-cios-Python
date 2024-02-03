'''Elabore um programa onde o usuário pode digitar quantas palavras quiser e depois
o programa exibe uma mensagem informando quais foram a primeira a última letra
da frase.'''

frase = input("Digite várias palavras separadas por espaço")

dialog = frase.split()

if len(dialog) > 0:
    prim_letra = dialog[0][0]
    ult_letra = dialog[-1][-1]

    print(f"A primeira letra da frase é '{prim_letra}' e a última letra é '{ult_letra}'")

else: 
    print("Nenhuma palavra foi colocada")