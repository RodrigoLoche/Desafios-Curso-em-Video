# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
#seno, cosseno e tangente desse ângulo.

import math

ang = float(input("Digite o valor de um ângulo: "))
ang_radiano = math.radians(ang)

print(f"O seno de {ang}° é {math.sin(ang_radiano):.2f}")
print(f"O cosseno de {ang}° é {math.cos(ang_radiano):.2f}")
# print(f"A tangente de {ang}° é {math.tan(ang_radiano):.2f}")

#  A tangente não existe para alguns ângulos, se o cosseno for zero, a tangente não existe. 
# Forma de resolver isso:

if abs(math.cos(ang_radiano)) < 1e-10: # notação científica 1e-10 = 0.0000000001: qualquer número menor que isso → praticamente zero
    print(f"A tangente de {ang}° não existe.")
else:
    print(f"A tangente de {ang}° é {math.tan(ang_radiano):.2f}")
