'''
Faça um programa que lê uma string e exibe “Palíndromo” caso a string seja um
palíndromo e “Não é palíndromo” caso não seja. Assuma que a entrada não tem
acentos e que todas as letras são minúsculas.
'''

def verify_palind(s):
    s = s.lower()
    s = s.replace(" ", "")

    return s == [::-1]

resposta = input("Digite aqui uma string: ")

if verify_palind(resposta):
    print("Sim. É Palíndromo")

else:
    print("Não é palíndromo")