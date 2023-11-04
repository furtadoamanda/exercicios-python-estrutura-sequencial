"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

arquivo = float(input("Qual o tamanho do arquivo para download em MB?"))
velocidade = float(input("Qual a velocidade do link de Internet em Mbps?"))

tempo_em_segundos = arquivo / velocidade
tempo_em_minutos = tempo_em_segundos / 60

print(f"O tempo em minutos para download de um arquivo de {arquivo} MB é de {tempo_em_minutos} minutos.")

