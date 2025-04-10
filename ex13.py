nome=input("escreva o nome completo do estudante: ")
idade=int(input("escreva a idade do estudante: "))
turma=input("escreva a turma do estudante: ")
if idade>=6:
    print(f"aluno cadastrado com sucesso:{nome},{idade} anos, turma {turma}")
else:
   print("A criança não tem idade suficiente para se matricular")