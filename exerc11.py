'''Crie um programa que executa apenas duas operações matemáticas: SOMA e
MULTIPLICAÇÃO.
1.1. O programa deve iniciar perguntando qual das operações o usuário deseja realizar. O programa
também deve oferecer uma opção para encerrar sem realizar nenhuma operação (digitar zero,
por exemplo). Caso o usuário informe uma opção que não seja uma das três listadas, o
programa deve informar novamente quais são as opções válidas.
1.2. Caso o usuário informe que a opção de finalizar o programa, basta exibir na tela uma
mensagem de encerramento e parar a execução.
1.3. Caso o usuário escolha uma das operações (SOMAR ou MULTIPLICAR), o programa deverá
efetuar a operação selecionada. O programa primeiramente solicita quantos números o usuário
deseja somar ou multiplicar e na sequência ele recebe os valores. Exemplo: usuário informa o
número cinco (cinco números). O programa então receberá cinco números para efetuar a soma
ou a multiplicação desses valores.
1.4. Após receber a quantidade de valores determinada o programa deve exibir como saída o
resultado da operação selecionada e, por fim, parar sua execução.'''
print('-=' * 13)
print('')
print('   Escolha uma opção   \n',
      '1 - Operar Soma \n',
      '2 - Operar Multiplicação \n',
      '0 - Encerrar')
print('')
print('=-' * 13)

while True:
    operation = int(input("Opção que deseja efetuar [1, 2, 0]: "))

    if operation == 1 or operation == 2:
        quantidade = int(input("Quantas vezes deseja operar? "))
        result = 0  # Inicializa o resultado

        for i in range(quantidade):
            numero = float(input(f"{i + 1} Número: "))

            if operation == 1:
                result += numero  # Soma
            elif operation == 2:
                if i == 0:
                    result = numero  # Inicializa o resultado com o primeiro número
                else:
                    result *= numero  # Multiplicação

        print("Resultado:", result)

    elif operation == 0:
        print("Aplicação encerrada! ")
        break

    else:
        print("Opção inválida. Tente novamente.")
