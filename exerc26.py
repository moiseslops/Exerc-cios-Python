'''
Escreva e teste uma função que recebe um número inteiro positivo e retorna o somatório de
todos os números menores ou igual a ele. Exemplo: número = 5, somatório = 1+2+3+4+5.'''

def soma(numero):
    if numero < 0:
        return "Número deve ser positivo"
    
    resultado = sum(range, 1, numero+1)
    return resultado

num_test = int(input("Digite um número positivo inteiro: "))
result = soma(num_test)

if type(result) == int:
    print(f"A soma dos números até {num_test} é: {result}")

else:
    print(result)