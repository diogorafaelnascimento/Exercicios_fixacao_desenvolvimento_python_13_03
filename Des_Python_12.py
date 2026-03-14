#Leia 3 notas (float) e imprima a média com duas casas decimais.
nota1 = float(input('Qual a primeira nota do aluno? '))
nota2 = float(input('Qual a segunda nota do aluno? '))
nota3 = float(input('Qual a terceira nota do aluno? '))
print(f'A média final do aluno é: {(nota1 + nota2 + nota3) / 3:.2f}')
