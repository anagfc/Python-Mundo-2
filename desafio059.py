n1 = float(input('Insira o 1º valor: '))
n2 = float(input('Insira o 2º valor: '))
opção = 0
while opção != 5:
    print('=' * 22)
    print('{:^22}'.format('Menu'.upper()))
    print('\n[1] Somar\n[2] Multiplicar\n[3] Exibir o maior\n[4] Mudar números\n[5] Sair')
    opção = int(input('Selecione uma opção: '))
    if opção == 1:
        soma = n1 + n2
        print('\n')
        print('=' * 22)
        print('{:^22}'.format('Soma'))
        print('\n   {} + {} = \033[1m{}\033[m\n'.format(n1, n2, soma))
    if opção == 2:
        multiplicação = n1 * n2
        print('\n')
        print('=' * 22)
        print('{:^22}'.format('Multiplicação'))
        print('\n   {} x {} = \033[1m{:.2f}\033[m\n'.format(n1, n2, multiplicação))
    if opção == 3:
        print('\n')
        print('=' * 22)
        print('{:^22}'.format('Maior número')) 
        if n1 > n2:
            print('\nO maior número é {}.\n'.format(n1))
        elif n2 > n1:
            print('\nO maior número é {}.\n'.format(n2))
        else:
            print('\n  Os dois são iguais.\n')
    if opção == 4:
        print('\n')
        n1 = float(input('Modifique o 1º valor: '))
        n2 = float(input('Modifique o 2º valor: '))
        print('\n')
print('=' * 22)
print('Encerrando...\n')
