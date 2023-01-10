print('\033[1mAnalisando números\033[m\n')
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
if n1 > n2:
    print('\nO 1º valor é o maior.')
elif n1 < n2:
    print('\nO 2º valor é o maior.')
else:
    print('\nNão existe um valor maior, os dois são iguais.')
