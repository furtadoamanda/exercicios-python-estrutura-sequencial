"""Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: 
(72.7*altura) - 58"""

altura = float(input("Qual a sua altura em metros?"))
peso_ideal = (72.7 * altura) - 58
peso_ideal_arredondado = "{:.2f}".format(peso_ideal)

print(f"O peso ideal para sua altura de {altura}m é {peso_ideal_arredondado}kg.")