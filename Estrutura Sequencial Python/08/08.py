"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

valor_horas = float(input("Quanto você ganha por hora?"))
horas_trabalhadas = float(input("Quantas horas você trabalha por mês?"))
salario = valor_horas * horas_trabalhadas

print(f"Seu salário mensal é R$ {salario}")