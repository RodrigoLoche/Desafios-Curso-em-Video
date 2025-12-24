# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

nomes = ["Joseph", "Maria", "Ronaldo", "Ana Flor"]
escolhido = random.choice(nomes)
print(f"Entre os alunos: {nomes}. O escolhido foi {escolhido}")
    
