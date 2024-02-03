class Pais:
   def __init__(self, nome, extensao, lista):
       self.nome = nome
       self.extensao = extensao
       self.lista = lista

   def paises(self):
       pais = 'Ásia'
       print('Países  entre', pais)
       l = ['Afeganistão', 'Armênia', 'Arábia Saudita']
       print('Países: ')
       print(l)
       for c in range(len(l)):
           c += 1
           p = input(f'País {c}, total de pessoas: ')
           ext = float(input(f'Extensão do território, país {c}: '))
           p += p
           ext += ext
           self.extensao = ext
           self.lista = p
       print(f'Total de pessoas {self.extensao}')
       print(f'Extensão territorial da soma de todos: {self.extensao}')


p1 = Pais('Ásia', 123.456, 'opa')
p1.paises()
