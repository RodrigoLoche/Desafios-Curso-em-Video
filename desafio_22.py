# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas.
# Quantas letras ao todo(Sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = input("Digite o seu nome: ").strip()
print(nome.upper()) # O nome com todas as letras maiúsculas
print(nome.lower()) # O nome com todas minúsculas.

print(len(nome))
print(len(nome.replace(" ",""))) # Quantas letras ao todo(Sem considerar espaços).

primeiro_nome = nome.split()
print(len(primeiro_nome[0]))# Quantas letras tem o primeiro nome.




 
