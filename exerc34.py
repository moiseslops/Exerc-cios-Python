class Triangulo:
   def __init__(self, base, altura, area):
       self.base = base
       self.altura = altura
       self.__area = area

   def criar_triangulo(self):
       print('=' * 20)
       print('Seu triângulo')
       print('=' * 20)

       while True:
           try:
               opcao = int(input('1 - Criar triângulo | 2 - calcular área | 3 - sair'))
               if opcao < 1 or opcao > 3:
                   print('Valor não disponível na opção.. Digite um valor válido')
               if opcao == 1:

                   b = float(input('Valor da base'))
                   alt = float(input('Valor da altura: '))
                   self.base = b
                   self.altura = alt
                   print('Triângulo criado...')
               elif opcao == 2:
                   b = float(input('Valor da base'))
                   alt = float(input('Valor da altura: '))
                   self.base = b
                   self.altura = alt

                   vl_area = (b * alt) / 2
                   self.__area = vl_area
                   print('A área do triângulo é: ', round(self.__area))

               elif opcao == 3:
                   print('Encerrado')
                   break

           except ValueError:
               print('O valor digitado não é um número. ')


t1 = Triangulo(12, 13, 14)
t1.criar_triangulo()
