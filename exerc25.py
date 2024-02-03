# Inicializa uma lista vazia para armazenar as notas dos alunos
notas_alunos = []

# Solicita ao usuário inserir 10 notas
for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas_alunos.append(nota)

# Calcula a média da turma
media_turma = sum(notas_alunos) / len(notas_alunos)

# Inicializa contadores para as diferentes categorias de notas
acima_de_60 = 0
abaixo_de_20 = 0
entre_21_e_59 = 0
nota_zero = 0

# Conta quantos alunos estão em cada categoria
for nota in notas_alunos:
    if nota > 60:
        acima_de_60 += 1
    elif nota < 20:
        abaixo_de_20 += 1
    elif 21 <= nota <= 59:
        entre_21_e_59 += 1
    elif nota == 0:
        nota_zero += 1

# Exibe os resultados
print("\nResultados:")
print(f"a) Média da turma: {media_turma:.2f}")
print(f"b) Alunos com nota acima de 60: {acima_de_60}")
print(f"c) Alunos com nota abaixo de 20: {abaixo_de_20}")
print(f"d) Alunos com nota entre 21 e 59: {entre_21_e_59}")
print(f"e) Alunos com nota zero: {nota_zero}")
