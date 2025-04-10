email_certo = input("crie um email")
email_certo =str.lower(email_certo)

senha=input("crie uma semha")
if len(senha) < 8 :
    print("senha muito pequena")
else:
    senha_correta = senha
    email=input("insira o email")
    email = str.lower(email)
    senha=input("insira a senha")
if email == email_certo:
    if senha == senha_correta:
         print("bem vindo")
else:
    print("Email ou senha incorretos")

