# Questão 6:

numero = int(input('Digite um número inteiro qualquer para ver a sua tabuada: '))
contador = 0

while contador <= 10:
    print('\n{} x {} = {}'.format(numero, contador, numero * contador))
    contador += 1
