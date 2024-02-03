quantidade_pessoas = int(input('Quantidade de
pessoas:'))
distancia_percorrida = int(input('Distância
percorrida: '))
preco_combustivel = float(input('Preço do
combustível: R$'))
media_de_consumo = int(input('Média de consumo:
'))
valor_1 = (distancia_percorrida *
preco_combustivel / media_de_consumo)
valor_2 = (valor_1 / quantidade_pessoas)
print('O valor da despesa para cada professor foi:
R${:.2f}'.format(valor_2))