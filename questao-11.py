# Questão 11:

def ler_valores_tempo_velocidade_media():
    tempo = int(input('Digite o seu tempo gasto na viagem, em horas: '))
    velocidade_media = float(input('Digite a sua velocidade média durante a viagem, em km/h: '))
    return (tempo, velocidade_media)

def calcular_distancia(tempo_gasto, velocidade_media_obtida):
    distancia = tempo_gasto * velocidade_media_obtida
    return distancia

def calcular_litros(distancia_percorrida):
    litros = distancia_percorrida / 12
    return litros

def mostrar_resultados(tempo, velocidade_media, distancia, litros):
    if tempo <= 0 and velocidade_media <= 0:
        print('\nNúmero(s) inválido(s)! Digite novamente')
    else:
        print('\nCom base no tempo {:.0f} h e na velocidade média {:.0f} km/h, as distância percorrida e quantidade de litros usados foram {:.0f} km e {:.1f} L nessa viagem'.format(tempo, velocidade_media, distancia, litros))

tempo_gasto, velocidade_media_obtida = ler_valores_tempo_velocidade_media()
distancia_percorrida = calcular_distancia(tempo_gasto, velocidade_media_obtida)
litros_usados = calcular_litros(distancia_percorrida)
mostrar_resultados(tempo_gasto, velocidade_media_obtida, distancia_percorrida, litros_usados)
