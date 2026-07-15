import string

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



def login():
    user = input("Nome de usuario ou E-mail: ")
    senha = input("Senha: ")
    
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
                    print("Usuario encontrado!")
                    break
            else:  
                print("usuario ou senha incorretos")
    except FileNotFoundError:
        print("Arquivo não encontrado")

#============================================================
#========================= Produtos =========================
#============================================================

def produto():
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
        compra = float(input("Valor de venda: R$"))
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
            unidade == "Kg"
        elif unidade == 2:
            unidade == "L"
        else: 
            unidade == "Unid"

        arquivo = open("Produtos", "a", encoding="utf-8")
        arquivo.write(f"Código: {codigo} | Descrição: {descricao} | Categoria: {categoria} {unidade} | Estoque: {armazem} | Valor de venda: R${compra:.2f} | Valor de venda: R${venda:.2f} \n")
        arquivo.close()