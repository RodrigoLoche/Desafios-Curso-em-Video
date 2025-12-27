# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o teceiro número: "))

maior = max(num_1, num_2, num_3)
menor = min(num_1, num_2, num_3)

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")
