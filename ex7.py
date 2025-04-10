num1 =int(input("insira o primeiro número"))
num2 =int(input("insira o segundo número"))
opcao = input("insira a operação desejada (soma, subtração, multiplicação, divisão)")
soma=num1+num2
sub=num1-num2
mult=num1*num2
div=num1/num2
if opcao == "soma":
    print(soma)
elif opcao == "subtração":
     print(sub)
elif opcao == "multiplicação":
     print(mult)
elif opcao == "divisão":
    print(div)
else:
     print("operação inválida")
