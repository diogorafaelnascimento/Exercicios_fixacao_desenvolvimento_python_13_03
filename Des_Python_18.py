#Leia um nome e uma nota (float), com uma casa decimal, e imprima: Aluno <nome> ficou com nota <nota>
aluno = input('Digite o nome do aluno: ')
nota = float(input('Digite o nota do aluno: '))
print(f'Aluno <{aluno}> ficou com nota <{nota:.1f}>')