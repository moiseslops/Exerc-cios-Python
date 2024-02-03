def preencher_lista(tamanho, primeiro_elemento):
    lista = [0] * tamanho  
    lista[0] = primeiro_elemento  

    for i in range(1, tamanho):
        lista[i] = lista[i - 1] / 2  

    return lista


tamanho_lista = int(input("Digite o tamanho da lista: "))
primeiro_elemento = float(input("Digite o primeiro elemento: "))


resultado_lista = preencher_lista(tamanho_lista, primeiro_elemento)


print("Conteúdo da lista:")
for elemento in resultado_lista:
    print(elemento)
