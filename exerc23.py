from prettytable import PrettyTable

print('-' * 20)
print('Mercado')
print('-' * 20)


class Pedido:
    def __init__(self, num_produto, description, vlr_unit, qtd_comp):
        self.num_produto = num_produto
        self.description = description
        self.vlr_unit = vlr_unit
        self.qtd_comp = qtd_comp

    def gerar_fatura(self):
        quant = int(input('Quantos produtos comprou: '))
        for q in range(quant):
            lista_produt = []
            lista = []
            vlr_unitario = float(input('Preco do produto: '))
            fatura = vlr_unitario * quant
            q += 1
            n_produt = float(input(f'Número do Produto {q}: '))
            lista.append(n_produt)
            d = input('Descrição do produto : ')
            lista_produt.append(d)

            print(f'fATURA: {fatura},\n'
                  f'Qtd.comprado: {quant}, \n'
                  f'Números dos produtos{lista},\n Preço do produto{lista_produt}')


def main():
    p1 = Pedido(12, 12, 12, 12)
    p1.gerar_fatura()


main()
