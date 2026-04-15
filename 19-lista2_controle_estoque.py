import os
os.system("cls")

print("exercicio controle de estoque")

produto_estoque = int(input("digite a quantidade em estoque: "))


if(produto_estoque >5):
    print("estoque baixo!")

else:
    print("estoque ok!")
