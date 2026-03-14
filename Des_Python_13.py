#Leia o salário (float) e um percentual de aumento (float) e calcule o novo salário.
salario = float(input('Digite o salário atual: '))
aumento = float(input('Digite o percentual de reajuste: '))
aumentof = (aumento / 100) + 1
print(f'Seu salário atual é de R${salario:.2f}, seu próximo salário terá um reajuste de {aumento:.2f}%, totalizando R${salario * aumentof:.2f} reajuste')