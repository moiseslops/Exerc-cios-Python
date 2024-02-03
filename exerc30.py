class Personagem:
    def __init__(self, nome, energia=100):
        self.nome = nome
        self.energia = energia

    def atacar(self):
        res = input('Deseja atacar? [s/n]')

        if res == 's':
            res = input('Atacar: ')
            while True:
                if res == 's':
                    val_energ = self.energia - (5 / 100)
                    self.energia = val_energ
                    print('Após o ataque, o personagem ficou com'
                          f'{self.energia}')
                    resposta = input('Deseja atacar de novo: ')
                    if resposta == 'n':
                        print(f'Não foi atacado. Energia em {self.energia}')
                        break

        else:
            print(f'Então a energia continua sendo {self.energia}')


class Guerreiro(Personagem):
    def __init__(self, forca, arma, nome, energia):
        super().__init__(nome, energia=100)
        self.energia = energia
        self.forca = forca
        self.arma = arma

    def adc_arma(self):
        # Armas
        print('Opção: 1[Arma]--- 2[Lança]')
        resp = int(input('Qual opção: 1/2'))
        if resp == 1:
            print('Arcenal')
            l = ['Espingarda', 'Pistola', 'Calibre 38']
            print(l)
            var = input('Qual arma: ')
            if var not in l:
                print('Não existe ')
            else:
                v_f = self.energia - (7 / 100)
                self.energia = v_f
                print(f'Energia caiu para {self.energia}')

        elif resp == 2:

            l_2 = ['Adaga', 'Espada', 'Machado']
            print(l_2)
            var = input('Tem alguma dessas armas? ')
            if var == 's':
                qst = input('Qual: ')
                if qst == 'Machado':
                    val = self.energia - (15 / 100)
                    self.energia = val
                    print(f'Energia foi para: {self.energia}')

                elif qst == 'Espada':
                    while True:
                        res = input('Atacar [s/n]: ')
                        if res == 's':
                            print('Dano de...')
                            val_f = self.energia - (10 / 100)
                            self.energia = val_f
                            print(f'Energia de: {self.energia}')
                            resposta = input('Deseja atacar de novo: ')

                            if resposta == 'n':
                                print(f'Não foi atacado. Energia em {self.energia}')
                                break

                        else:
                            print(f'Energia de {self.energia}')
                            break
                else:
                    while True:
                        resp = input('Atacar com essa arma? ')
                        if resp == 's':
                            print('Não envolve nenhuma das')
                            val_ene = self.energia - (7 / 100)
                            self.energia = val_ene
                            print(f'Energia foi  para {self.energia}')
                            resposta = input('Deseja atacar de novo: ')

                            if resposta == 'n':
                                print(f'Não foi atacado. Energia em {self.energia}')
                                break
                        else:
                            print(f'Energia de {self.energia}')
                            break
            else:
                ener = self.energia - (7 / 100)
                self.energia = ener
                print('Não tem essa arma')
                print(f'A energia foi para {self.energia}')


# Importando classe Pai

p1 = Personagem('Tony Stark', 55)
p1.atacar()

# Importando a classe filha

p2 = Guerreiro(156, 'Espingarda', 'Moisés', 100)
p2.adc_arma()