# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

speed = int(input("Digite uma velocidade: Km/h "))

if speed > 80:
    print(f"Você estava {speed - 80} km/h acima do limite.")
    print(f"Você foi multado! A multa vai custar R${(speed - 80) * 7.00:.2f}")
else:
    print("Velocidade permitida!")   
    
