import os
os.system("cls")
print("bem vindo a escola aprender!")
nivel_professor = int(input("digite seu nivel (1,2 ou 3):"))
aulas_semana = int(input("digite a quantidade de aulas: "))

if nivel_professor ==1:
    valor_hora = 12
elif nivel_professor ==2:
    valor_hora = 17
elif nivel_professor ==3:
    valor_hora = 25
else:
    print("nivel invalido!")

pagamento = valor_hora * aulas_semana

print(f"voce deu :{aulas_semana} aulas")
print(f"voce é professor nivel: {nivel_professor}")

print(f"total a receber : {pagamento}")