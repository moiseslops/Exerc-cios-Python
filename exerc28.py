class Carro:
    def __init__(self, km, viajem):
        self.km = km
        self.viajem = viajem

    def distanciaPercorrida(self):
        km = float(input('Quilometragem do carro:'))
        d = float(input('Qual a distância percorrida: '))

        var = km + d
        print(f'O carro tem ao final: {var}km')


def main():
    c1 = Carro(12, 'Cidade')
    c1.distanciaPercorrida()


main()
