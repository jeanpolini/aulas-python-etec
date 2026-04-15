import os 
import random
import time


os.system("cls")

vida_jogador = 100
vida_inimigo = 100

print("bem vindo a batalha pokemon em python!")
nome = input("informe seu nome: ")


while(vida_jogador > 0 and vida_inimigo> 0):
    os.system("cls")
    print(f"vida: {vida_jogador} | vida inimigo: {vida_inimigo}")

    print("faça sua jogada")
    print("[1] - atacar")
    print("[2] - curar")
    print("[3] - fugir")

    op_jogador = int(input("escolha uma opção :"))
    op_inimigo = random.randint(1,3)

    #atacou
    if(op_jogador == 1):
        vida_inimigo -= 10
    #curou
    elif(op_jogador == 2):
        vida_jogador += 5    

    #fugiu    
    elif(op_jogador == 3):
        print("voce fugiu!")
        vida_jogador = 0
    print("iniciando a jogada do inimigo em 3 segundos.")
    time.sleep(3)
    
        #turno do inimigo
    if(op_inimigo == 1):
        print(f"o inimigo escolheu: atacar!")
        time.sleep(3)
        vida_jogador  -= 10
    elif(op_inimigo ==2):
        print("o inimigo escolheu: curar")
        time.sleep(3)
        vida_inimigo += 5
    elif(op_inimigo == 3):
        print("o inimigo escolheu : fugir!") 
        vida_inimigo = 0
        time.sleep(3)   
#verificando quem foi o ganhador
if(vida_jogador > vida_inimigo):
    print("parabens voce ganhou!")

else:
    print("game over - voce perdeu!")

