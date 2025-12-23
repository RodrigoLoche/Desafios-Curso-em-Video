# Desafio 004

# Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

algo = input("Digite algo: ")

print(f"O tipo primitivo é: {type(algo)}")
print(f"É alfanúmerico? {algo.isalnum()}")
print(f"É apenas númerico? {algo.isnumeric()}")
print(f"Está em maiúsculo? {algo.isupper()}")
print(f"Está em minúsculo? {algo.islower()}")
print(f"Apenas a primeira letra é maiúscula? {algo.istitle()}")
print(f"Tem apenas espaços? {algo.isspace()}")
