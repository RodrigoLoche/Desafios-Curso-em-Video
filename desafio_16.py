# Crie um programa que leia um número Real qualquer pelo telcado e mostre na tela
#a sua porção inteira. 

# EX:> Digite um numero:6.127
# O número 6.127 tem a parte inteira 6


import math

num = float(input("Write a number: "))
print(f"O numero inteiro de {num} é {math.trunc(num)}")



from math import trunc

num = float(input("Write a number: "))
print(f"O numero inteiro de {num} é {trunc(num)}")
