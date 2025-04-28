# Questão 7:

numeros = []

for i in range(5):
    numero = int(input('Digite cinco números inteiros qualquer, um por caixa de texto: '))
    numeros.append(numero)

for numero in numeros:
    soma += numero

print('\nCom base nos números {:.0f}, {:.0f}, {:.0f}, {:.0f} e {:.0f}, a sua soma é {:.0f}'.format(numeros[0], numeros[1], numeros[2], numeros[3], numeros[4], soma))
