import os
os.system("cls")

print("exercicio ano bissexto")

ano = int(input("digite um ano:"))

if ano % 4 == 0:
    print("ano bissexto!")
else:
    print("nao é bissexto!")
        