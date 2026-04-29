import os
import time
os.system("cls")

senha = int(input("digite sua senha : "))
if senha == 1234:
    print("aceso liberado!")
else:
    print("senha invalida!")
    print("comece novamente!")
    exit()


saldo_cliente_inicial = 1000
continuar = True



print("exercicio caixa eletronico.")
while(continuar == True):

    print("===Menu===")
    print("[1]- saque")
    print("[2] - deposito")
    print("[3]- saldo")
    print("[4]-sair")

    

    opcao = int(input("escolha uma opção: "))
    time.sleep(3)

    #verificar opçao escolhida
    if(opcao ==1):
        
        print("saque")
        valor_saque =int(input("digite o valor do saque :"))
        calcular_saque = saldo_cliente_inicial - valor_saque
        saldo_cliente_inicial = calcular_saque
        time.sleep(3)
        print(f"saque solicitado de r$: {valor_saque}")
        print(f"saldo atual r$: {calcular_saque}")
    elif(opcao ==2):
        
        print("deposito")
        valor_deposito =int(input("digite o valor a ser depositado :"))
        calcular_deposito = saldo_cliente_inicial + valor_deposito
        saldo_cliente_inicial = calcular_deposito
        time.sleep(3)
        print(f"valor depositado de r$ :{valor_deposito}")
        print(f"saldo atual r$ : {calcular_deposito}")
    elif(opcao == 3):
        print("saldo") 
        calcular_saldo = saldo_cliente_inicial
        time.sleep(3)
        print(f"seu saldo atual é r$ :{saldo_cliente_inicial}")   
    else:
        opcao==4
  
        continuar == False
        print("sistema encerrado") 
        break