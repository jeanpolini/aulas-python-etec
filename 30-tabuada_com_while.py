import os
os.system("cls")

print("super tabuada com while!")

numero = int(input("digite um numero :"))
intervalo = int(input("digite o fim do intervalo :"))
contador = 0

while(contador <= intervalo):
    print(f"{numero} x {contador} = {numero * contador}")
    contador+=1
    
