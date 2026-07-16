import string
import tkinter as tk

#============================================================
#=========================== Login ==========================
#============================================================

def nova_conta():
    maiusculo = string.ascii_uppercase
    numero = string.digits
    especial = string.punctuation
    while True:
        user = input("Nome de usuário: ")
        email = input("E-mail: ")
        print("A senha deve conter pelomenos uma letra maiúscula, número e caractere especial!")
        senha = input("Senha: ")

        if (set(senha) & set(maiusculo)) and (set(senha) & set(numero) and (set(senha) & set(especial))):
            conf_senha = input("Confirme a senha: ")
            if senha == conf_senha:
                
                arquivo = open("funcionarios.txt", "a", encoding="utf-8")
                arquivo.write(f"Usuário: {user} | Senha: {senha} | E-mail: {email} \n")
                arquivo.close()
                print("Novo usuário cadastrado!")

                break
            else:
                print("Senha incorreta!")
        else:
            print("Senha não segue as credenciais!")



def login(user, senha):
    """ user = input("Nome de usuario ou E-mail: ")
    senha = input("Senha: ") """
    
    try:
        funcionarios = open("funcionarios.txt", "r", encoding="utf-8")
        dados = funcionarios.readlines()
        funcionarios.close()

        if dados == "":
            print("Usúarios não cadastrados!")
        else:
            for i in dados:
                info = i.strip().split(" | ")
                dados_user = info[0].split(": ")[1]
                dados_senha = info[1].split(": ")[1]
                dados_email = info[2].split(": ")[1]

                if (user == dados_user or user == dados_email) and senha == dados_senha:
                    texto(tela_login, "Usuario encontrado!")

                    return True
            else:  
                print("usuario ou senha incorretos")
    except FileNotFoundError:
        texto(tela_login, "Arquivo não encontrado")
        

#============================================================
#========================= Produtos =========================
#============================================================

def cadastra_produto():
    try:
        codigo = input("Código: ")
        descricao = input("Descrição: ")

        print("""
        1. Hortifruti
        2. Carnes
        3. Gelados
        """)
        categoria = int(input("Categoria: "))
        if categoria < 1 or categoria > 3: raise(ValueError("A opção não é um valor valido."))

        print("""
        1. Kg
        2. L
        3. unid   
        """)
        unidade = int(input("Meio de medidade: "))
        if unidade < 1 or unidade > 3: raise(ValueError("A opção não é um valor valido."))

        armazem = float(input("Estoque atual: "))
        compra = float(input("Valor de compra: R$"))
        venda = float(input("Valor de venda: R$"))
    except:
        print("Dado não fornecido corretamente!")
    else:
        if categoria == 1:
            categoria = "Hortifruti"
        elif categoria == 2:
            categoria = "Carnes"
        else:
            categoria = "Gelados"
        
        if unidade == 1:
            unidade = "Kg"
        elif unidade == 2:
            unidade = "L"
        else: 
            unidade = "Unid"

        arquivo = open("produtos.txt", "a", encoding="utf-8")
        arquivo.write(f"Código: {codigo} | Descrição: {descricao} | Categoria: {categoria} | Estoque: {armazem:.2f}{unidade} | Valor de venda: R${compra:.2f} | Valor de venda: R${venda:.2f} \n")
        arquivo.close()

        print("Produto cadastrado")

def lista_produto():
    try:
        produtos = open("produtos.txt", "r", encoding="utf-8")
        dados = produtos.read()
        produtos.close()
    except:
        print("Lista de produtos não encontrada!")
    else:
        print(dados)

#============================================================
#========================== Tkinter =========================
#============================================================

interface = tk.Tk()
interface.geometry("800x500")
interface.title("Sistema de Produtos")


def telas(tela, verdade):
    if verdade == True:
        tela_login.pack_forget()
        tela_cconta.pack_forget()

        tela.pack(fill="both", expand=True)
    else:
        texto(tela, "Dados incorretos")
        

def texto(tela, conteudo):
    mensagem = tk.Label(tela, text=f"{conteudo}")
    mensagem.pack()

#===================== Frame 1 - Login ======================

tela_login = tk.Frame(interface)

texto(tela_login, "Usúario ou E-mail: ")
user = tk.Entry(tela_login)
user.pack()

texto(tela_login, "Senha: ")
senha = tk.Entry(tela_login)
senha.pack()

def confirmar():
    user_confirme = user.get()
    senha_confirme = senha.get()

    verdade = login(user_confirme, senha_confirme)
    telas(tela_login, verdade)

botao_confirmar = tk.Button(tela_login, text="Confirmar", command=confirmar)
botao_confirmar.pack()

#=================== Frame 2 - Criar conta ==================
tela_cconta = tk.Frame(interface)

texto(tela_cconta, "Sucesso!!!")

telas(tela_login, True)
                 
interface.mainloop()
    