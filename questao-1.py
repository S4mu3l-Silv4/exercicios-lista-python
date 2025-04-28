# Questão 1:

numero_1 = float(input('Digite um número qualquer: '))
numero_2 = float(input('Digite um segundo número qualquer: '))

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2

print('\nAs soma, subtração, multiplicação e divisão dos números {:.3f} e {:.3f} são {:.3f}, {:.3f}, {:.3f} e {:.3f}, respectivamente'.format(numero_1, numero_2, soma, subtracao, multiplicacao, divisao))
