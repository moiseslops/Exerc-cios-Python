
class Retangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def areaRetangulo(self):
        base = float(input('Base do retângulo: '))
        altura = float(input('Altura do retângulo: '))

        area = (base * altura) / 2
        perimetro = (base + altura) * 2

        print(f'A área do retângulo é: {area}')
        print(f'O perimetro do retângulo é: {perimetro}') 

def main():

    rtg1 = Retangulo(12, 12)
    rtg1.areaRetangulo()


main()
