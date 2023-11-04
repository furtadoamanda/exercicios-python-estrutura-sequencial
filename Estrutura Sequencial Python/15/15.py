"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    1. salário bruto.
    2. quanto pagou ao INSS.
    3. quanto pagou ao sindicato.
    4. o salário líquido.
    5. calcule os descontos e o salário líquido, conforme a tabela abaixo:Obs.: Salário Bruto - Descontos = Salário Líquido.
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$ """

valor_hora = float(input("Quanto você ganha por hora?"))
horas_trabalhadas = float(input("Qual o número de horas trabalhadas no mês?"))

salario_bruto = valor_hora * horas_trabalhadas

imposto_de_renda = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto

salario_liquido = salario_bruto - imposto_de_renda - inss - sindicato

print(f"+ Salário Bruto : R$ {salario_bruto} \n - IR (11%) : R$ {imposto_de_renda} \n - INSS (8%) : R$ {inss} \n - Sindicato (5%) : R$ {sindicato} \n = Salário Líquido : R$ {salario_liquido}")