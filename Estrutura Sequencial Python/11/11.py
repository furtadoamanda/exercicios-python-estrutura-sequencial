"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    1. o produto do dobro do primeiro com metade do segundo .
    2. a soma do triplo do primeiro com o terceiro.
    3. o terceiro elevado ao cubo."""

inteiro1 = int(input("Insira um número inteiro: "))
inteiro2 = int(input("Insira outro número inteiro: "))
real = float(input("Insira um número real: "))

produto = (2 * inteiro1) * (inteiro2 / 2)

soma = (3 * inteiro1) + real

potencia = real ** 3


print(f"O produto do dobro do primeiro com metade do segundo é {produto}")

print(f"A soma do triplo do primeiro com o terceiro é {soma}")

print(f"O terceiro elevado ao cubo é igual a {potencia}")

