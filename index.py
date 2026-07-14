import string


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
                arquivo.write(f"Usuário: {user} | Senha: {senha} | E-mail:{email} \n")
                arquivo.close()
                print("Novo usuário cadastrado!")

                break
            else:
                print("Senha incorreta!")
        else:
            print("Senha não segue as credenciais!")

def login():
    user = input("Nome de usuario: ")
    senha = input("Senha: ")

nova_conta()