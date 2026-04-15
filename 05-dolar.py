import os
os.system("cls")

# 1 etapa entrada de dados 
print("atividade conversor de dollar para real")
quantia_dolar = float(input("entre com uma quantidade de dollar ($):"))

cotacao_dollar = float(input("digite a cotação do dollar do dia;"))

# 2 etapa processamento

total_em_reais = quantia_dolar * cotacao_dollar

#3 saida
print(f"o valor total em reais R$:{total_em_reais:.2F} ")