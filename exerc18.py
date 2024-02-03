'''Crie um programa que receba uma mensagem digitada pelo usuário e informe a ele
quando o texto ultrapassar 280 caracteres.'''

mensage = input("Coloque aqui sua mensagem: ")

if len(mensage) > 280:
    print("A mensagem ultrapassou 280 caracteres")
else: 
    print("A mensagem tem um comprimento aceitável")