import string
import tkinter as tk
from tkinter import filedialog

#============================================================
#===================== conta - nova conta ===================
#============================================================

def nova_conta(user, email, senha, conf_senha):
    maiusculo = string.ascii_uppercase
    numero = string.digits
    especial = string.punctuation

    if (set(senha) & set(maiusculo)) and (set(senha) & set(numero) and (set(senha) & set(especial))):
            
            if senha == conf_senha:
                
                arquivo = open("funcionarios.txt", "a", encoding="utf-8")
                arquivo.write(f"Usuário: {user} | Senha: {senha} | E-mail: {email} \n")
                arquivo.close()
                texto(tela_cconta, "Novo usuário cadastrado!", 10)

                telas(tela_login)
            else:
                texto(tela_cconta, "Senha incorreta!", 10)
    else:
        texto(tela_cconta, "Senha não segue as credenciais!", 10)

#=====================Conta - Login ======================

def login(user, senha):
    
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
                    texto(tela_login, "Usuario encontrado!", 50)

                    telas(tela_menu)
            else:  
                texto(tela_login, "Usúario ou senha incorretos", 50)
    except FileNotFoundError:
        texto(tela_login, "Arquivo não encontrado", 50)
        

#============================================================
#============== Produtos - cadastrar produtos ===============
#============================================================

def cadastra_produto(codigo, descricao, categoria, armazem, unidade, compra, venda):
    

    arquivo = open("produtos.txt", "a", encoding="utf-8")
    arquivo.write(f"Código: {codigo} | Descrição: {descricao} | Categoria: {categoria} | Estoque: {float(armazem):.2f}{unidade} | Valor de compra: R${float(compra):.2f} | Valor de venda: R${float(venda):.2f} \n")
    arquivo.close()

    telas(tela_menu)

    print("Produto cadastrado")

#============== Produtos - lista de produtos ===============

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


def telas(tela):
    tela_login.pack_forget()
    tela_cconta.pack_forget()
    tela_menu.pack_forget()
    tela_produtos.pack_forget()
    tela_registrar.pack_forget()

    tela.pack(fill="both", expand=True)

        

def texto(tela, conteudo, px):
    mensagem = tk.Label(tela, text=f"{conteudo}")
    mensagem.pack(pady=(px))


def botao(tela, texto, command, px):
    botao_confirmar = tk.Button(tela, text=f"{texto}", command=command)
    botao_confirmar.pack(pady=(px))



#===================== Frame 1 - Login ======================

tela_login = tk.Frame(interface)

texto(tela_login, "Usúario ou E-mail: ", 10)
user = tk.Entry(tela_login)
user.pack(pady=(1))


texto(tela_login, "Senha: ", 10)
senha = tk.Entry(tela_login)
senha.pack(pady=(1))

def conf_login():
    user_confirme = user.get()
    senha_confirme = senha.get()

    login(user_confirme, senha_confirme)


botao(tela_login, "Entrar", conf_login, 50)

tk.Button(tela_login, text="Criar conta", command=lambda: telas(tela_cconta)).pack(pady=(1))

#=================== Frame 2 - Criar conta ==================
tela_cconta = tk.Frame(interface)

texto(tela_cconta, "Usúario: ", 10)
c_user = tk.Entry(tela_cconta)
c_user.pack(pady=(1))

texto(tela_cconta, "Email: ", 10)
c_email = tk.Entry(tela_cconta)
c_email.pack(pady=(1))

texto(tela_cconta, "Senha:", 10)
c_senha = tk.Entry(tela_cconta)
c_senha.pack(pady=(1))
texto(tela_cconta, "OBS: A senha deve conter pelomenos uma letra maiúscula, número e caractere especial!", 1)

texto(tela_cconta, "Confirmar senha: ", 10)
conf_senha = tk.Entry(tela_cconta)
conf_senha.pack(pady=(1))

def conf_criacao():
    user = c_user.get()
    email = c_email.get()
    senha = c_senha.get()
    senha_conf = conf_senha.get()

    nova_conta(user, email, senha, senha_conf)

botao(tela_cconta, "Registrar", conf_criacao, 10)
tk.Button(tela_cconta, text="Login", command=lambda: telas(tela_login)).pack()

#=================== Frame 3 - menu ==================
tela_menu = tk.Frame(interface)

tk.Button(tela_menu, text="Ver produtos", command=lambda: telas(tela_produtos)).pack(pady=(50))
tk.Button(tela_menu, text="Registrar", command=lambda: telas(tela_registrar)).pack(pady=(5))
tk.Button(tela_menu, text="Sair", command=lambda: telas(tela_login)).pack(pady=(50))

#=================== Frame 4 - ver produtos ==================
tela_produtos = tk.Frame(interface)

""" produtos = open("produtos.txt", "r", encoding="utf-8")
lista = produtos.read()
produtos.close()

texto(tela_produtos, lista, 10) """

tk.Button(tela_produtos, text="Sair", command=lambda: telas(tela_menu)).pack(pady=5) 


#=================== Frame 5 - Registrar ==================
tela_registrar = tk.Frame(interface)

texto(tela_registrar, "Código: ", 10)
codigo = tk.Entry(tela_registrar)
codigo.pack(pady=(1))

texto(tela_registrar, "Descrição: ", 10)
descricao = tk.Entry(tela_registrar)
descricao.pack(pady=(1))

texto(tela_registrar, "Categoria: ", 10)
categoria = tk.Listbox(tela_registrar, exportselection=False)
categoria.pack(pady=(1))
categoria.insert(tk.END, "Hortifruti")
categoria.insert(tk.END, "Carnes")
categoria.insert(tk.END, "Gelados")

texto(tela_registrar, "Meio de medidade: ", 10)
medida = tk.Listbox(tela_registrar, exportselection=False)
medida.pack(pady=(1))
medida.insert(tk.END, "kg")
medida.insert(tk.END, "L")
medida.insert(tk.END, "Unid.")

texto(tela_registrar, "Estoque atual: ", 10)
armazem = tk.Entry(tela_registrar)
armazem.pack(pady=(1))

texto(tela_registrar, "Valor de compra: ", 10)
compra = tk.Entry(tela_registrar)
compra.pack(pady=(1))

texto(tela_registrar, "Valor de venda: ", 10)
venda = tk.Entry(tela_registrar)
venda.pack(pady=(1))


def conf_registro():
    c_codigo = codigo.get()
    c_descricao = descricao.get()
    c_categoria = categoria.curselection()
    i_categoria = categoria.get(c_categoria)
    c_medida = medida.curselection()
    i_medida = medida.get(c_medida)
    c_armazem = armazem.get()
    c_compra = compra.get()
    c_venda = venda.get()

    cadastra_produto(c_codigo, c_descricao, i_categoria, c_armazem, i_medida, c_compra, c_venda)



botao_regitrar = tk.Button(tela_registrar, text="registrar", command=conf_registro)
botao_regitrar.pack(side=tk.LEFT, padx=500, pady=5)

tk.Button(tela_registrar, text="Sair", command=lambda: telas(tela_menu)).pack(side=tk.LEFT, padx=0, pady=5)

telas(tela_login)
                 
interface.mainloop()
    