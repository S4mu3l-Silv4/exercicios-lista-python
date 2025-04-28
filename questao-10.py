# Questão 10:

def ler_valor_celsius():
    celsius = float(input('Digite uma temperatura qualquer em Celsius para ver a sua conversão em Fahrenheit: '))
    return celsius

def calcular_celsius_para_fahrenheit(celsius):
    fahrenheit = (9 * celsius + 160) / 5
    return fahrenheit

def mostrar_resultado(graus_fahrenheit, graus_celsius):
    print('\nA conversão de {:.1f} graus Celsius é {:.1f} graus Fahrenheit'.format(graus_celsius, graus_fahrenheit))

temperatura_celsius = ler_valor_celsius()
temperatura_fahrenheit = calcular_celsius_para_fahrenheit(temperatura_celsius)
mostrar_resultado(temperatura_fahrenheit, temperatura_celsius)
