import os
os.system("cls")

# 1 etapa - realizar as entradas 

print("seja bem vindo ao boletim virtual")

nota01 = float(input("entre com a primeira nota:"))
nota02 = float(input("entre com a segunda nota:"))
nota03 = float(input("entre com a terceira nota:"))

# 2 etapa - processamento

media = (nota01 + nota02 + nota03) /3

if(media >= 6):
    print("voce foi aprovado!")

elif(media >= 4 and media <= 5):
    print("o aluno esta de recuperação!")    
else:
    print("voce foi reprovado")

# 3 etapa - saida - exibir o resultado

print(f"sua média foi:{media}")



