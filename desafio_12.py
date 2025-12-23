# Desafio 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_produto = float(input("Digite o preço do produto: R$"))
desconto = preco_produto * 5 / 100 
preco_desconto = preco_produto - desconto
print(f"O produto com 5% de desconto irá custar R${preco_desconto:.2f}")
