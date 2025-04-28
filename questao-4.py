# Questão 4:

nota_1 = float(input('Digite a sua primeira nota: '))
nota_2 = float(input('Digite a sua segunda nota: '))
nota_3 = float(input('Digite a sua terceira nota: '))

media = (nota_1 + nota_2 + nota_3) / 3

if media < 0:
    print('\nMédia inválida! Digite novamente')
elif media >= 0 and media < 4:
    print('\nSua média é {:.1f}, você foi reprovado'.format(media))
elif media >= 4 and media < 6:
    print('\nSua média é {:.1f}, você pegou exame'.format(media))
    exame = float(input('Digite a sua nota do exame: '))
    if exame < 6:
        print('\nSua nota do exame é {:.1f}, você foi reprovado'.format(exame))
    else:
        print('\nSua nota do exame é {:.1f}, parabéns! Você foi aprovado'.format(exame))
else:
    print('\nSua média é {:.1f}, parabéns! Você foi aprovado'.format(media))
