tentativas = 0
right_user = "mtfg2025"
right_password = "159734862"
while tentativas < 3:
    login_user = input("Digite seu usuário: ")
    login_password = input("Digite sua senha: ")
    if login_user == right_user and login_password == right_password:
        print("Login realizado com sucesso! Bem vindo ao aplicativo :)")
        break
    else:
        if tentativas == 2:
            for _ in range(3):
                print("Acesso bloqueado")
            break
        print(f"Erro! Tentativa Nº{tentativas+1}. Ainda restam {2 - tentativas} tentativas..")
        tentativas += 1

