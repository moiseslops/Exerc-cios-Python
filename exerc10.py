xico = 0
tiao = 0
xuxa = 0
print("[1] Xico [2] Tião [3] Xuxa [4] Branco [0] Encerrar a votação")
opcao = 0
resp = 0
voto = 0
nulo = 0
while True:
    voto = int(input("Qual a sua opção?"))
    if voto == 1:
        xico += 1
    if voto == 2:
        tiao += 1
    elif voto == 3:
        xuxa += 1
    elif voto == 0:
        print("Votação encerrada")
    break
print("xico tem {} votos".format(xico))
print("Tiao tem {} votos".format(tiao))
print("Xuxa tem {} votos".format(xuxa))