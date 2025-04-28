# Questão 2:

tempo = float(input('Digite o seu tempo gasto na viagem, apenas o número em horas: '))
velocidade_media = float(input('Digite a sua distância percorrida na viagem, apenas o número em km: '))

if tempo <= 0:
    print('\nNúmero(s) inválido(s)! Digite novamente')
elif velocidade_media <= 0:
    print('\nNúmero(s) inválido(s)! Digite novamente')
else:
    distancia = tempo * velocidade_media
    litros = distancia / 12
    print('\nOs valores de tempo gasto, velocidade média, distância percorrida e litros utilizados na viagem são {:.0f} h, {:.0f} km/h, {:.1f} km e {:.1f} L, respectivamente'.format(tempo, velocidade_media, distancia, litros))
