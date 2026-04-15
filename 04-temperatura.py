import os
os.system("cls")
# 1 etapa entradas 
print("conversor de temperaturas")
print("seja bem vindo!")

nome_usuario = input("entre com seu nome:")
print("ola",nome_usuario)
# 2 etapa processamento

temperatura_celsius = float(input("entre com a temperatura celsius:"))

temperatura_Fanhrenheit=(9*temperatura_celsius+160)/5

# 3 etapa - saida

print(f"a temperatura convertida em fanhrenheit é:{temperatura_Fanhrenheit}")
