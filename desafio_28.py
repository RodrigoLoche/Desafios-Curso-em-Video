# Escreva um programa que faça o computador "Pensar" em uum número inteiro
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

num = random.randint(0, 5)
guess = int(input("Adivinhe o número que o computador pensou de (0 á 5): "))

if guess == num:
    print("Você acertou!")
else:
    print(f"Você errou! o número era {num}.")
    
