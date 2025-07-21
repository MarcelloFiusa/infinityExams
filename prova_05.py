turma = {}

while True:
    try:
        qtde_alunos = int(input("Digite o número de alunos da turma: "))
        for _ in range(qtde_alunos):
            notas = []
            nome_aluno = input("digite o nome do aluno: ")
            for i in range(3):
                while True:
                    try:
                        nota = float(input(f"Digite a {i+1}ª nota do aluno: "))
                        notas.append(nota)
                        break
                    except ValueError:
                        print("Valor deve ser numeral!")
            turma[nome_aluno] = notas
        break
    except ValueError:
        print("Valor não válido! Quantidade de alunos deve ser inteiro!")

media_geral = []
for aluno, notas in turma.items():
    if notas:
        media = sum(notas) / len(notas)
        media_geral.append(media)
        if media >= 7:
            print(f"{aluno} Está Aprovado com média {media:.2f}! Suas notas foram:")
            print(*notas)
        else:
            print(f"{aluno} Está Reprovado com média {media:.2f}!")
media_geral_turma = sum(media_geral) / len(media_geral)
print(f"Media geral da turma foi: {media_geral_turma}")


