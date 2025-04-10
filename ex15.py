nome_produto = input("digite o nome do produto: ")
quantidade = int(input("insira a quantidade comprada: "))
preco = float(input("digite o preço: "))
valor_total = quantidade * preco
desconto5 = valor_total - valor_total*0.05
if valor_total <=100:
    print(f"Total R${valor_total}")
else:
    print(f"Total: R${desconto5}")
