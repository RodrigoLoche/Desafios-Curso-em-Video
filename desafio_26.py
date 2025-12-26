# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra "A"
# Em que posição ela apare a primeira vez.
# Em que posição ela aparece a última vez.


frase = input("Escreva uma frase: ").strip().upper()
print(frase.count("A"))

print(f"A primeira letra 'A' apareceu na posição: {frase.find('A') + 1}") # + 1 para ficar na contagem (humana);

print(f"A última letra 'A' apareceu na posição: {frase.rfind('A') + 1}")
