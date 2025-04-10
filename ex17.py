anonascimento=int(input("digite seu ano de nascimento"))
anoatual=int(input("digite o ano atual"))
idade = anoatual - anonascimento
if anonascimento>anoatual:
    print("tentativa incorreta,o ano de nascimento é maior que o ano atual.")
elif idade >= 18:
    print("voce é maior de idade ", idade ,"anos ")
else:    
    print("voce é menor de idade", idade ,"anos")
