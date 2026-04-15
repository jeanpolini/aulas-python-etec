import os
os.system("cls")

#1 etapa -entradas
print("atividade - habilitação")

idade = int(input("digite sua idade:"))

if(idade >= 18):
    habilitacao = input("voce possui habilitação: (sim ou nao):")
    
    if(habilitacao == "sim"):
        print("o usuario pode dirigir!")
    else:
        print("voce não possui habilitação pra dirigir!")    
else:
    print("voce nao pode dirigir!")     
