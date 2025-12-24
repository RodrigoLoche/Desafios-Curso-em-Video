#Escreva um programa que pergunte a quantidade de km percorridos por um carro
#alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e 
#R$0,15 por km rodado.

dias = int(input("Quantos dias alugado: "))
km_rodado = float(input("Quantos Km foram rodados? "))
p_day = 60
p_km = 0.15 
total = (dias * p_day) + (km_rodado * p_km)
print(f"O valor total do aluguel ficou em: R${total:.2f}")
