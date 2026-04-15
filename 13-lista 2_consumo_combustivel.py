import os
os.system("cls")

print("atividade consumo combustivel.")

quilometros_rodados = float(input("digite quantos quilometros percorreu :"))
combustivel_gasto = float(input("digite quantos litros de combustivel utilizou: "))


consumo = quilometros_rodados / combustivel_gasto

print(f"consumo medio do seu veiculo foi de  {consumo} km por litro.")

