import os
os.system("cls")

def exibir_menu():
   
    print("[1] - real para dolar")
    print("[2] - dolar para real")
    print("[3] - sair")

def converter_real_para_dolar(quantia_real, taxa_dolar):    
    total_dolar = quantia_real / taxa_dolar
    return total_dolar

def converter_dolar_para_reais(quantia_dolar, taxa_dolar):
    total_reais = quantia_dolar * taxa_dolar
    return total_reais

def sair():
    input("obrigado por utilizar o sistema, pressione <enter> para sair ..")
    exit()

while True:

    print("seja bem vindo ao conversor de moedas!")
    #chamando a funçao exibir_menu
    exibir_menu()


    opcao = int(input("escolha uma opção: "))

    if(opcao ==1):
        os.system("cls")
        print("===conversao de real para dolar===")
        quantia_real = float(input("informe a quantia de R$:"))
        taxa_dolar = float(input("informe a cotação do dolar $: "))

        total_dolar = converter_real_para_dolar(quantia_real,taxa_dolar)

        print(f"o total de dolares convertidos é: ${total_dolar}")
        print("pressione <enter> para continuar")

    elif(opcao ==2):
        os.system("cls")
        print("===conversao de dolar para real===")
        quantia_dolar = float(input("informe a quantia de $:"))
        taxa_dolar = float(input("informe a cotação do dolar R$:"))

        total_reais = converter_dolar_para_reais(quantia_dolar, taxa_dolar)  
        print(f"o total de reais convertidos é R$:{total_reais}") 

    #sair
    elif(opcao ==3):
        sair()
