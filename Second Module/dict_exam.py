usuario = {
    'nome': '',
    'telefone': '',
    'email': '',
}

nome = input("Insira seu nome de contato: ")
telefone = input("Insira o telefone para contato: ")
email = input("Insira o email de contato: ")

usuario['nome'] = nome
usuario['telefone'] = telefone
usuario['email'] = email

for info, contato in usuario.items():
    print(f"{info}: {contato}")