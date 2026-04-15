import os
os.system("cls")

print("atividade numero negativo ou positivo")

numero = int(input("digite um numero:"))

if(numero > 0):
    print(f"o numero {numero} é positivo")

elif(numero < 0): 
     print("numero negativo")


  
else:
    print(f"o numero {numero} é neutro")
