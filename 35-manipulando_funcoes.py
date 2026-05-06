import os
import funcoes
os.system("cls")




print("manipulando funçoes com python.")

# chamando a função exibir_menu
funcoes.exibir_menu()

opcao = int(input("escolha uma das opções:"))

numero1 = float(input("digite o primeiro numero:"))
numero2 = float(input("digite o segundo numero:"))


if(opcao == 1):
    # chamar a função somar
    total = funcoes.somar(numero1,numero2)
    print(f"a soma é: {total}")

elif(opcao ==2):
    #chamar a funçao subtrair
    print(f"a subtração é:{funcoes.subtrair(numero1, numero2)}")    

elif(opcao ==3):
    #chamar a funçao multiplicar
    total = funcoes.multiplicar(numero1,numero2)
    print(f"a multiplicação é;{total}")    

elif(opcao ==4):
    #chamar a funçao dividir
    print(f"a divisão é;{funcoes.dividir(numero1,numero2)}")  

else:
    print("operação invalida!")