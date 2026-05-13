import os 
#======================
#ver catalogo
#======================
def exibir_catalogo(filmes):
    os.system("cls")
    print("=== catalogo de filmes ===")
    
    

#========================
#carregar menu do admin
#========================
def carregar_menu_admin():
    os.system("cls")
    print("=== autenticação ===")
    usuario = input("informe seu usuario :")
    senha = input("informe sua senha:")

    if(usuario != "admin" and senha != "123"):
        input("acesso negado!")
        return
    while True:
        os.system("cls")
        print("=== menu do administrador===")
        print("[1]- cadastrar filme ")
        print("[2]- ver catalogo")
        print("[3]- top e flop")
        print("[4]- voltar")

        op= int(input("escolha uma opção: "))

        if(op ==1):
            os.system("cls")
            print("=== cadastro de filmes ===")
            titulo = input(" titulo do filme: ")
            genero = input("informe o genero: ")

            filme = {
                "titulo": titulo,
                "genero": genero,
                "avaliacoes": [],
                "media": 0,
                "classificacao": "sem classificação",
                "disponivel": True,
                "cliente": None
             }
            
            filmes.append(filme)
            print("filme cadastrado com sucesso")
            input("pressione <enter> para continuar")


        elif(op ==4):
            break



        

#================
#sistema principal
#=================
os.system("cls")

# lista de fimes (banco de dados)
filmes = []

while True:
    os.system("cls")
    print("=== bem vindo a locadora cineflix ===")
    print("[1]- entrar como cliente")
    print("[2]- entrar como administrador")
    print("[3]- sair")
    op = int(input("escolha uma opção: "))

    if(op ==1):
        print("entrou como cliente ")

    elif(op ==2):
        print("entrou como administrador")
        carregar_menu_admin()

    elif(op ==3):
        print("obrigado por utilizar o sistema")
        input("pressione <enter> para sair.")
        break

