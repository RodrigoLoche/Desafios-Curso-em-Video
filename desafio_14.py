# Escreva um programa que converta uma temperatura digitada em °C
# e converta para °F.

temp_c = float(input("Digite temperatura em °C: "))
conv = (temp_c * 1.8) + 32
print(f"{temp_c:.2f}°C em Fahrenheit é: {conv:.2f}°F")
