import os
os.system("cls")

    


print("bem vindo ao restaurante prato cheio!")
def menu_pagamento():
    print("===Escolha forma de pagamento===")
    print("[1]- dinheiro")
    print("[2]- VR")
    print("[3]- cartão")
    print("[4]- sair")
    

quantidade_pessoas = int(input("digite a quantidade de pessoas:"))

valor_original_conta= float(input("digite o valor total da conta R$: "))

porcentagem_garcom = valor_original_conta * 10 / 100
taxa_vr = valor_original_conta * 2 / 100
taxa_cartao = valor_original_conta * 3 /100



while True:

    menu_pagamento

    opcao = int(input("escolha uma opção:"))
    os.system("cls")

    if(opcao ==1):
        print("dinheiro")
       
        print(f"valor da conta R$:{valor_original_conta}")
        print(f"taxa do garcom R$:{porcentagem_garcom}")
        soma = valor_original_conta + porcentagem_garcom
        print(f"valor total com taxas R$:{soma}")
        divisao = soma / quantidade_pessoas
        print(f"valor por pessoa R$: {divisao}")

    elif(opcao ==2):
        print("VR")
        print(f"valor da conta R$:{valor_original_conta}")
        print(f"taxa do garcom R$:{porcentagem_garcom}")
        soma = valor_original_conta + porcentagem_garcom + taxa_vr
        print(f"taxa do vr R$: {taxa_vr}")
        print(f"valor total com taxas R$:{soma}")
        divisao = soma / quantidade_pessoas
        print(f"valor por pessoa R$: {divisao}")
    elif(opcao ==3):
        print("cartao")
        print(f"valor da conta R$: {valor_original_conta}") 
        print(f"taxa do garçom R$: {porcentagem_garcom}")   
        soma = valor_original_conta + porcentagem_garcom + taxa_cartao
        print(f"taxa do cartão R$:{taxa_cartao}")
        print(f"valor total com taxas R$: {soma}")
        divisao = soma / quantidade_pessoas
        print(f"valor por pessoa R$: {divisao}")
    else:
        opcao ==4
        print("sistema encerrado")
        break        
