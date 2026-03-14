#Leia o preço de um produto e imprima o preço com 10% de desconto.
preco = float(input('Qual o valor do produto? '))
print(f'O preço do produto é R${preco}, com 10% de desconto fica R${preco * 0.9:.2f}')