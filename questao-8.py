# Questão 8:

alunos = {}

for i in range(3):
    aluno = input('Digite os nomes dos alunos, um por caixa de texto: ')
    nota = float(input('Digite a nota dele(a): '))
    alunos[aluno] = nota

soma_notas = sum(alunos.values())
media = soma_notas / len(alunos)

if media < 0:
    print('\nMédia inválida! Digite novamente')
else:
    print('\nA média dessas notas é {:.1f}'.format(media))
