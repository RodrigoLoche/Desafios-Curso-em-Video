# Desafio 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo sálario, com 15% de aumento.


salario = float(input("Digite seu salário: R$"))
aumento = salario * 0.15
novo_salario = salario + aumento
print(f"Seu novo salário com 15% de aumento ficará em R${novo_salario:.2f}")


salario = float(input("Digite seu salário: R$"))
print(f"Seu novo salário com 15% de aumento ficará em R${salario * 1.15:.2f}")

#Quando você dá 15% de aumento, isso significa:
# 100% → salário original
# +15% → aumento
# Total = 115%
# 115% = 115 / 100 = 1.15
