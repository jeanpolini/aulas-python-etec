import os
os.system("cls")

print("atividade tempo de estudo")

horas_estudo_dia = float(input("digite quantas horas por dia voce estuda: "))


if(horas_estudo_dia <=2):
    print("pouco estudo!")

elif(horas_estudo_dia >2 and horas_estudo_dia<4):
    print("medio estudo!")  

elif(horas_estudo_dia > 5):   
    print("muito estudo!")    