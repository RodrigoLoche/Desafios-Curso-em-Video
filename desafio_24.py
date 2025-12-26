#Crie um programa que leio o nome de uma cidade e diga se
#ela começa ou não com o nome "SANTO"

# Forma 1 

cidade = input("Digite o nome de uma cidade: ").upper()
encontre = cidade.find("SANTO", 0, 5)
if encontre == -1:
    print("A cidade NÃO começa com a palavra 'Santo'")
else:
    print("A cidade COMEÇA com Santo")
    
    
# Forma 2

cidade = input("Digite o nome de uma cidade: ").strip().upper()

if cidade.startswith("SANTO"):
    print("A cidade COMEÇA com Santo")
else:
    print("A cidade NÃO começa com Santo")



# Forma 3


cidade = input("Digitie o nome de uma cidade: ").upper()
encontre = cidade.find("SANTO")


if encontre == -1:
    print("A Cidade NÃO tem a palavra Santo")
elif encontre == 0:
    print("A cidade COMEÇA com Santo")
else:
    print("A cidade NÃO começa com a palavra 'SANTO' ")
    

