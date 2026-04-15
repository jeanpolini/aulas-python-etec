import os 
os.system("cls")

print("atividade produtos")

produto = input("digite o nome do produto:")
quantidade = int(input("digite a quantidade adquirida:"))
preco_unitario = float(input("digite o preco unitario:"))

total = quantidade * preco_unitario


if(quantidade <=5 ):
    desconto = total * 2/100
elif(quantidade >5 and quantidade <=10):
    desconto = total *3/100
elif(quantidade >10):
    desconto = total *5/100

total_desconto = total - desconto

print(f"voce comprou: {produto}")
print(f"adquirido: {quantidade}")
print(f"no valor de : {total}")
print(f"valor com desconto: {total_desconto} ")

