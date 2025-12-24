# O mesmo professor do desafio anterior quer sortear a ordem de apresentação
#de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a  ordem sorteada.

import random

nomes = ["Joseph", "Maria", "Ronaldo", "Ana Flor"]
random.shuffle(nomes) #shuffle() não retorna nada. Ele modifica a lista no lugar, Por isso isso não funcionaria dessa forma > nomes = random.shuffle(nomes)  # errado
print(f"A ordem da apresentação entre os 4 alunos é: {nomes}")
