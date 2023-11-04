"""Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = 32 + (9 * (celsius / 5))


print(f"{celsius} ºC são {fahrenheit} ºF")

# Quero usar a função que arredonda em um número x de casas decimais, não consigo achar qual é a função 