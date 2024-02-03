'''Crie um programa que receba uma frase do usuário e informe quantas palavras há
na frase.'''

frase = input("Digite aqui sua frase: ")

number = len(frase.split())

print("Número de palavras dentro da frase: ", number)