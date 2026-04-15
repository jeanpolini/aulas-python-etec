import os
os.system("cls")

print("exemplo com while - salario do professor")

resposta = "sim"

while True:
    os.system("cls")

    print("=== menu ===")
    print("[1] - calcular o salario")
    print("[2] - sair do programa")

    opcao = int(input("escolha uma opcao :"))

    # verificando qual foi opçao escolhida
    if(opcao == 1):  
        os.system("cls")     
        print("qual é o nivel do professor")
        print("[1]-nivel 1")
        print("[2]-nivel 2")
        print("[3]-nivel 3")
        

        nivel = int(input("escolha um nivel :"))

        if(nivel >=4):
             print("nivel invalido!")
             input("pressione <enter> para continuar...")
             continue
        else:
         qtd_aulas = int(input("digite a quantidade de aulas :"))

        if(nivel == 1):
            salario = qtd_aulas * 12
        elif(nivel == 2):
             salario = qtd_aulas * 17
        elif(nivel == 3):
            
            salario = qtd_aulas * 25
         
        else:
            print("nivel invalido!")
            input("pressione <enter> para continuar...")
            continue

        print(f"o salario do professor sera {salario}") 
        input("pressione <enter> para continuar...")

    elif(opcao ==2):
        input("pressione enter para encerrar o programa...")
        break

print("finalizou o programa!")    
