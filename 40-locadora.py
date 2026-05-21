import os 


# sistema principal 

os.system("cls")


def exibir_catalogo(filmes):
    os.system("cls")
    print("   catalogo de filmes   ")

    for item in filmes:
        print(f"titulo: {item['titulo']}")
        print(f"genero: {item['genero']}")
        print(f"média: {item['media']}")
        print(f"classificação: {item['classificacao']}")
        print(f"avaliaçoes: {item ['avaliacoes']}")
        
        if(item['disponivel'] == True):
            status = "Disponivel para Alugar"
        else:
            status = f"Alugado pelo cliente {item['cliente']}"

        print(f"Status: {status}")

        

        print("==========================")

def alugar_filme(filmes):

    os.system("cls")
    print("=== Alugar filme ===")
    titulo = input("Digite o nome do filme: ")

    for item in filmes:
        if item['titulo'].lower() == titulo.lower():

            if(item['disponivel'] == True):
                nome = input("Nome do cliente:")
                item['disponivel'] = False
                item['cliente'] = nome
                print("Filme Alugado com sucesso!")
                input("pressione <enter> para continuar...")
            else:
                print(f"Filme Já Alugado pelo cliente {item['cliente']}")
                print("pressione <enter> para continuar...")
            return
        
def calcular_media(avaliacoes):
    media = sum(avaliacoes) /len(avaliacoes)
    return round(media,1)

def classificar_filme(media):
    if media >=8:
        return "muito bom!"
    elif media >=5 and media <8:
        return "mais ou menos!"
    else:
        return "flop!"
    
def melhor_filme(filmes):
    return max(filmes,key=lambda item: item['media'])  
def pior_filme(filmes) :
    return min(filmes,key=lambda item: item['media'])



def devolver_filme(filmes):
    os.system("cls")
    print("=== devolver filmes ===")

    titulo = input(" digite o nome do filme para devolver:")
    for item in filmes:
        if item['titulo'].lower() == titulo.lower():
            if item['disponivel'] == False:
                print(f" o filme estava com cliente: {item['cliente']}")

                
                nota = float(input(" de uma avaliação de 0 a 10:"))
                item['avaliacoes'].append(nota)
                item['media'] = calcular_media(item['avaliacoes'])
                item['classificacao'] = classificar_filme(item['media'])

                item['disponivel']=True
                item['cliente']=None
    input("pressione <enter> para continuar")




def carregar_menu_cliente():
    os.system("cls")
    print("=== MENU DO CLIENTE ===")
    print("[1] - ver catalogo")
    print("[2] - Alugar Filme")
    print("[3] - Devolver Filme")
    print("[4] - Voltar")

    op = int(input("Escolha uma opção:"))

    if(op == 1):
        exibir_catalogo(filmes)
        input("Pressione Enter para Continuar..")
    elif(op == 2):
        alugar_filme(filmes)
    elif(op ==3):
        devolver_filme(filmes)   


def carregar_menu_adimin():
    os.system("cls")
    print(" autenticação ")
    usuario = input("digite seu nome de usuario:  ")
    senha = input("informe sua senha:  ")

    if(usuario != "adimin" and senha != 123):
        input("acesso negado")
        return
    
    while True:
        os.system("cls")
        print("MENU DO ADIMINISTRADOR")
        print("[1] - cadastrar filme")
        print("[2] - ver catalogo")
        print("[3] - top e flop")
        print("[4] - voltar")

        op = int(input("selecione uma opção:  "))

        if(op == 1):
            os.system("cls")
            print("cadastro dos filmes")
            titulo = input("titulo do filme:  ")
            genero = input("genero do filme:  ")

            filme = {

                "titulo": titulo,
                "genero": genero,
                "avaliacoes": [],
                "media": 0,
                "classificacao": "sem avaliações",
                "disponivel": True,
                "cliente": None,

            }

            filmes.append(filme)
            print("filme colocado com sucesso")
            input("pressione ENTER  para continuar....")

        elif(op == 2):
            exibir_catalogo(filmes)
            input("pressione ENTER para continuar")

        elif(op ==3):
            print(f" melhor filme: {melhor_filme(filmes)}")
            print(f"pior filme: {pior_filme(filmes)}")
            input("pressione ENTER para continuar...")
        
       


        elif(op == 4):
            break



# listas de filmes - banco de dados

filmes = [
    {
        "titulo": "A Origem",
        "genero": "Ficção Científica",
        "avaliacoes": [],
        "media": 0,
        "classificacao": "sem avaliações",
        "disponivel": True,
        "cliente": None,
    },
    {
        "titulo": "Interestelar",
        "genero": "Ficção Científica",
        "avaliacoes": [],
        "media": 0,
        "classificacao": "sem avaliações",
        "disponivel": True,
        "cliente": None,
    },
    {
        "titulo": "O Poderoso Chefão",
        "genero": "Drama",
        "avaliacoes": [],
        "media": 0,
        "classificacao": "sem avaliações",
        "disponivel": True,
        "cliente": None,
    },
    {
        "titulo": "Vingadores: Ultimato",
        "genero": "Ação",
        "avaliacoes": [],
        "media": 0,
        "classificacao": "sem avaliações",
        "disponivel": True,
        "cliente": None,
    },
    {
        "titulo": "Toy Story",
        "genero": "Animação",
        "avaliacoes": [],
        "media": 0,
        "classificacao": "sem avaliações",
        "disponivel": True,
        "cliente": None,
    },
    {
        "titulo": "Titanic",
        "genero": "Romance",
        "avaliacoes": [],
        "media": 0,
        "classificacao": "sem avaliações",
        "disponivel": True,
        "cliente": None,
    },
    {
        "titulo": "Coringa",
        "genero": "Drama",
        "avaliacoes": [],
        "media": 0,
        "classificacao": "sem avaliações",
        "disponivel": True,
        "cliente": None,
    },
    {
        "titulo": "Matrix",
        "genero": "Ação",
        "avaliacoes": [],
        "media": 0,
        "classificacao": "sem avaliações",
        "disponivel": True,
        "cliente": None,
    },
    {
        "titulo": "Parasita",
        "genero": "Suspense",
        "avaliacoes": [],
        "media": 0,
        "classificacao": "sem avaliações",
        "disponivel": True,
        "cliente": None,
    },
    {
        "titulo": "Shrek",
        "genero": "Comédia",
        "avaliacoes": [],
        "media": 0,
        "classificacao": "sem avaliações",
        "disponivel": True,
        "cliente": None,
    }
]

while True:
    os.system("cls")

    print("BEM VINDO A LOCADORA CINEFLIX ")
    print("[1] - entrar como cliente")
    print("[2] - entrar como administrador")
    print("[3] - sair")

    op = int(input("escolha uma opção:   "))

    if(op == 1):
        print("entrou como cliente")
        carregar_menu_cliente()
    
    elif(op == 2):
        carregar_menu_adimin()
        

    elif(op == 3):
        print("obrigado por usar o sistema")
        input("pressione <enter> para sair...")
        break

