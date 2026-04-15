import os
os.system("cls")

print("seja bem vindo!")
print("para efetuar login")


usuario = input("digite seu usuario: ")


if(usuario == "admin"):
    senha = (input("digite sua senha:"))

    if(senha == "123"):
    
      print("acesso permitido")
    else:
       print("sua senha esta incorreta") 
else:
    print("acesso negado")
   