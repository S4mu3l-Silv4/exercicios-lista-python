# Questão 5:

notas = []

for i in range(5):
    nota = float(input('Digite as suas notas, uma por caixa de texto: '))
    notas.append(nota)

media = sum(notas) / len(notas)

if media < 0:
    print('\nNota(s) inválida(s)! Digite novamente')
else:
    print('\nCom base nas notas {:.1f}, {:.1f}, {:.1f}, {:.1f} e {:.1f}, a sua média é {:.1f}'.format(notas[0], notas[1], notas[2], notas[3], notas[4], media))
