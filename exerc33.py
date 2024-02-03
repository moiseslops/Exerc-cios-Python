class Carro:
    def __init__(self, consumo):
        self.__consumo = consumo
        self.__combustivel = 0

    def adcionarGasolina(self, qualquer):
        self.__combustivel += qualquer

    def andar(self, km):
        maximo = self.__consumo * self.__combustivel
        if self.__combustivel:
            if km > maximo:
                print('Não tem o suficiente')
            else:
                var = km / self.__consumo
                self.__combustivel -= var
                print(f'Após andar {km} km, o carro possui \n'
                      '', round(self.__combustivel))
        else:
            print('Sem combustível')

    @property
    def combustivel(self):
        return self.__combustivel

    @combustivel.setter
    def combustivel(self, var):
        self.__combustivel -= var

    @property
    def consumo(self):
        return self.__consumo

    @consumo.setter
    def consumo(self):
        return self.__consumo