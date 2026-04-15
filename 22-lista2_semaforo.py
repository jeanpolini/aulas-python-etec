import os 
os.system("cls")

cor = input("digite uma cor (verde,amarelo ou vermelho :)")

if(cor == "verde"):
    print("pode passar!")
elif(cor == "amarelo"):
    print("atençao")    
elif(cor == "vermelho"):
    print("pare")
else:
    print("cor invalida")

