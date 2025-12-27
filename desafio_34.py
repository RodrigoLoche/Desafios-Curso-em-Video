# Escreva um programa que pergunte o sálario de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%


# Forma 1
salario = float(input("Qual é o seu salário? R$"))

if salario > 1250.00:
    print(f"O seu sálario com um aumento de 10% será de: R${(salario * 0.10) + salario:.2f}")
elif salario <= 1250.00:
    print(f"O seu sálario com um aumento de 15% será de: R${(salario * 0.15) + salario:.2f}")
    
    
# Forma 2
salario = float(input("Qual é o seu salário? R$"))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novo_salario = salario + aumento
print(f"Seu novo salário será de: R${novo_salario:.2f}")


