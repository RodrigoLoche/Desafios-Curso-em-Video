# Crie um programa que leia o nome de uma pessoa e diga se ela
#tem "SILVA" no nome.

# Forma 1
nome = input("Digite o seu nome completo: ").upper()
encontre = nome.find("SILVA")
if encontre == -1:
    print("Não tem SILVA no nome")
else:
    print("Tem SILVA no nome")
    
    
# Forma 2
nome = input("Digite o seu nome completo: ").strip().lower()
print(f"Seu nome tem Silva? {"silva" in nome}")
