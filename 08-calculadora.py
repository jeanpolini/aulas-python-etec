import os
os.system("cls")

print("atividade - calculadora")

numero01 = float(input("digite o primeiro numero:"))
numero02 = float(input("digite o segundo numero:"))

print("escolha uma das operações")

print("+ - adição")
print("- - subtração")
print("* - multiplicação")
print("/ - divisão")

operacao = input("informe a operação:")

if(operacao == "+"):
    resultado = numero01 + numero02

elif(operacao == "-"):
    resultado = numero01 - numero02

elif(operacao == "*"):
    resultado = numero01 * numero02

elif(operacao =="/"):
    resultado = numero01 / numero02   
else:
    print("operação invalida!") 

print("=" * 30)    
print(f"operação escolhida: {operacao}")
print(f"resultado: {resultado}")


