# notas do aluno
n1 = int(input('Nota 1: '))
n2 = int(input('Nota 2: '))
n3 = int(input('Nota 3: '))
n4 = int(input('Nota 4: '))
# pesos dos bimestres
p1 = p2 = 2
p3 = p4 = 3
# cálculo da média
media = int((n1*p1 + n2*p2 + n3*p3 + n4*p4)/(p1+p2+p3+p4))
# verificando a situação do aluno
if media >= 60:
    print('Aluno aprovado')
elif media >= 20:
    print('Aluno em recuperação')
else:
    print('Aluno reprovado')