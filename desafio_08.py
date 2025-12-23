# Desafio 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.

metros = float(input("Digite um valor em METROS: "))
centimetros = metros * 100
milimetros = metros * 1000

print(f"{metros:.2f} m = {centimetros:.2f} cm")
print(f"{metros:.2f} m = {milimetros:.2f} mm")
