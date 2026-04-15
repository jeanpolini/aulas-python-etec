import os
os.system("cls")

print("exercicio intervalo numerico")

numero = int(input("digite um numero:"))
print(f"voce escolheu numero : {numero}")

if(numero  >9 and numero  <51):
    print("esta entre 10 e 50!")
else:
    print("fora do intervalo!")    