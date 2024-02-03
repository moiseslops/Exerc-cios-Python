class ContaCorrente:
   def __init__(self, v_inicial, saldo):
       self.v_inicial = v_inicial
       self.saldo = saldo

   def saque(self):
       v_cont = float(input('Dinheiro da conta: '))
       s = float(input('Digite aqui o valor do saque: '))

       saq = v_cont - s
       print(f'Sobrou na conta após o saque de R${s}, sobrou: R${saq}')
   def saldoConta(self):
       dep = float(input('Depósito da conta: '))
       saque = float(input('Valor do saque da conta: '))

       saldo = dep - saque

       print(f'O saldo da conta é de: {saldo}')


def main():
   c1 = ContaCorrente(12, 12)
   c1.saque()
   c1.saldoConta()


main()

