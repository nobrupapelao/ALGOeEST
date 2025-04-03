nome=input("coloque o nome do aluno ") #aqui a variavel nome esta recebendo o input que é o valor que o usuario vai digitar
idade=int(input("coloque sua idade "))
turma=input("qual turma pertence ")
if idade>=6:
    print(f"aluno cadastrado com sucesso {nome}, {idade} anos, turma {turma}")
else: # senao
    print("A crianca nao tem idade o sufiientye para estudar")
