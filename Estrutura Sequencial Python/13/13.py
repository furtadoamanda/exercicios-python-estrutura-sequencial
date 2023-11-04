"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    1. Para homens: (72.7*h) - 58
    2. Para mulheres: (62.1*h) - 44.7"""

altura = float(input("Qual a sua altura em metros?"))
genero = int(input("Você é (1) homem ou (2) mulher?"))

peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7

peso_ideal_homem_arredondado = "{:.2f}".format(peso_ideal_homem)
peso_ideal_mulher_arredondado = "{:.2f}".format(peso_ideal_mulher)

if (genero == 1):
    print(f"Você é um homem de altura {altura}cm. Seu peso ideal é {peso_ideal_homem_arredondado}kg.")
elif (genero == 2):
    print(f"Você é uma mulher de altura {altura}cm. Seu peso ideal é {peso_ideal_mulher_arredondado}kg.")
