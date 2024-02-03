cobertura_tinta = 3
capacidade_lata = 18
preco_da_lata = 150.0
tamanho_area = float(input('Digite o tamanho daárea a ser pintada (em m2): '))
litros = tamanho_area / cobertura_tinta
latas_inteiras = int(litros / capacidade_lata)
if(litros%capacidade_lata != 0):
    latas_inteiras += 1

valor_total = (latas_inteiras * preco_da_lata)
print('Quantidade de latas necessárias: ',
latas_inteiras)
print('Valor total da compra: R$', valor_total)