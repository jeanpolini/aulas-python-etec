
import os
os.system("cls")

# 1 passo - variaveis e entradas 
print("calculadora de desconto")

nome_produto = input("entre com nome do produto:")
preco = float(input("entre com preço do produto:"))
percentual_desconto = float(input("entre com percentual do desconto %:"))

#2 passo - processamento
valor_desconto = preco * percentual_desconto / 100 
preco_final = preco - valor_desconto

#3 passo - exibir a saida
print("=============================")
print("preço original", preco, "- preço com descono", preco_final)
print(f"preço original:R${preco} - preço com desconto: {preco_final}")
