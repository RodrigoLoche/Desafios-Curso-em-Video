# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km
#para viagens de até 200km e R$0,45 para viagens mais longas.


distancia = float(input("Qual é a distância da viagem? km "))

if 0 < distancia <= 200:
    preco1 = distancia * 0.50
    print(f"O valor da sua passagem é R${preco1:.2f}")
elif distancia > 200:
    preco2 = distancia * 0.45
    print(f"O valor da sua passagem é R${preco2:.2f}") 
else:
    print("Distância incorreta!")
