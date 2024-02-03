'''Escreva um programa que recebe uma string S e dois inteiros i e j. O programa
então exibe a substring S[i, j]. O programa deve verificar se os números digitados
não ultrapassam o tamanho do texto. Caso isso ocorra, o programa deve solicitar
novamente os números.'''

def pegar_my_strings(s, i, j):
    while i < 0 or j >= len(s) or i > j:
        print("Índices inválidos. Verifique se o i >= 0, o j < comprimento de string e i <= j")
        i = int(input("Digite o valor de i: "))
        j = int(input("Digite o valor de j: "))

    sub = s[i:j+1]
    return sub

s = input("Digite aqui a string: ")

i = int(input("Digite o valor de i: "))
j = int(input("Digite o valor de j: "))

res = pegar_my_strings(s, i, j)

print(f"Sua substring  S[{i}, {j}] é {res}")