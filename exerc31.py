from datetime import date
from prettytable import PrettyTable


class Pessoa:
   def __init__(self, idade, nome, nascimento, fales):
       self.idade = idade
       self.nome = nome
       self.nascimento = nascimento
       self.fales = fales

   def calcula_idade(self):
       i = int(input('Ano de nascimento: '))
       print('Data atual...')
       data_atual = date.today()
       data = '{} / {} / {}'.format(data_atual.day, data_atual.month,
                                             data_atual.year)
       print('Data atual', data)
       idade = data_atual.year - i
       self.idade = idade
       print(f'Idade: {self.idade}')

       nome = input('Nome: ')
       self.nome = nome

       #status
       res = input('Mostrar status [s/n]')
       if res == 's':

           print('Status...')
           tabela = PrettyTable()
           tabela = PrettyTable(["Nome", "idade"])
           tabela.add_row([f"{self.nome}", f"{self.idade}"])
           print(tabela)

       else:
           if res == 'n':
               print('Processo de status não utilizado')

   def caso_vivos(self):
       print('Para o caso que esteja morto.')
       res = input('Estão Vivos? [s/n]')
       if res == 's':
           print('Está vivo, ação do programa concluída')

       elif res == 'n':
           nasc = int(input('Ano de nascimento: '))
           i = int(input('Ano de falescimento: '))
           data_atual = date.today()
           data = '{} / {} / {}'.format(data_atual.day, data_atual.month,
                                        data_atual.year)
           print('Data atual', data)
           fin = ((data_atual.year - i) - nasc) * -1
           var = data_atual.year - fin
           self.idade = var
           nome = input('Nome: ')
           self.nome = nome
           print(f'Se {self.nome} estivesse vivo, teria: {self.idade} anos')


p1 = Pessoa(12, 'Adan byron', '12/04/2006', '12/09/2050')
p1.calcula_idade()
p1.caso_vivos()
