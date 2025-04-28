# Questão 3:

idade = int(input('Digite a sua idade, apenas o(s) ano(s): '))

if idade < 0:
    print('\nIdade inválida! Digite novamente')
elif idade >= 0 and idade <= 12:
    print('\nDe acordo com a sua idade você ainda é criança')
elif idade >= 13 and idade <= 17:
    print('\nDe acordo com a sua idade você é adolescente')
elif idade >= 18 and idade <= 59:
    print('\nDe acordo com a sua idade você é adulto')
else:
    print('\nDe acordo com a sua idade você já é idoso')
