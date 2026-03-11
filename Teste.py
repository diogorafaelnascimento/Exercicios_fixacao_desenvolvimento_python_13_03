print('-=' * 21)
print('Cálculo do Índice de Massa Corporal (IMC)')
print('-=' * 21)
nome = input('\nDigite seu nome: ')
peso = float(input('Qual é seu peso atual (Kg)? '))
altura = float(input('Qual a sua altura (M)? '))
imc = peso / (altura ** 2)
print(f'O IMC de {nome} é {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você está dentro da faixa de peso ideal')
elif imc >= 25 and imc < 30:
    print('Você está na faixa de sobrepeso')
elif imc >= 30:
    print('Você está a faixa de obesidade')