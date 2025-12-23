# Desafio 011
# Faça um programa que leia a largura e a altura em metros, calcule a sua área
# e a quantidade de tinta necessária  para pintá-la, sabendo que cada litro de tinta,
# pinta uma área de 2m²

largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura
print(f"Você vai precisar de {area / 2:.2f} litros de tinta para uma área de {area} m².")
