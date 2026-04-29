import os
os.system("cls")

def escrever_msg(mensagem):
    print(mensagem)

def somar(n1,n2):
    resultado = n1+n2
    print (f"a soma é {resultado}")


#chamando a funçao
mensagem = input("digite uma mensagem:")
escrever_msg(mensagem)

somar(10,2)
somar(30,7)