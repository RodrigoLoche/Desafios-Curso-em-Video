# Desafio 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar.
# Considere US$1.00 =  R$3.27

money = float(input("Quantos R$ você tem: "))
print(f"Com R${money:.2f} você consegue comprar US${money / 3.27:.2f}")
