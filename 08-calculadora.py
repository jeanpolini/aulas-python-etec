import os
os.system("cls")

print("atividade - calculadora")

continuar = "sim"


while(continuar == "sim"):


    numero01 = float(input("digite o primeiro numero:"))
    numero02 = float(input("digite o segundo numero:"))

    print("escolha uma das operações")

    print("+ - adição")
    print("- - subtração")
    print("* - multiplicação")
    print("/ - divisão")
    print("[0] - sair")

    operacao = input("informe a operação:")

    if(operacao == "+"):
        resultado = numero01 + numero02

    elif(operacao == "-"):
        resultado = numero01 - numero02

    elif(operacao == "*"):
        resultado = numero01 * numero02

    elif(operacao =="/"):
        resultado = numero01 / numero02   

    elif(operacao =="0"):
        continuar = "nao"
        exit()
            
    else:
        print("operação invalida!") 

    print("=" * 30)    
    print(f"operação escolhida: {operacao}")
    print(f"resultado: {resultado}")


