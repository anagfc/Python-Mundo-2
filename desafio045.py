from random import choice
from time import sleep
nome_jogo = 'Jokenpô'
título1 = '  Você     vs   Computador'
print('--x--' * 7)
print('{:^35}'.format(nome_jogo).upper())
print('--x--' * 7)
print('1- Estou pronto!')
print('2- Regras')
print('3- Sair')
opção = int(input('Selecione: '))
if opção == 1:
    jogador = input('Qual sua escolha? ').upper()
    opções = ['PEDRA', 'PAPEL', 'TESOURA']
    computador = choice(opções).upper()
    print('--x--' * 7)
    sleep(0.5)
    print('{:^35}'.format('jo').upper())
    sleep(0.5)
    print('{:^35}'.format('ken').upper())
    sleep(0.5)
    print('{:^35}'.format('pô!').upper())
    sleep(0.5)
    print('-----' * 7)
    print('{:^35}'.format(nome_jogo).upper())
    print('-----' * 7)
    print('{:^35}\n'.format(título1))
    print('{:>12}'.format(jogador.upper()), end="    x    ")
    print('{}'.format(computador))
    if jogador == computador:
        print('\n{:-^34}'.format('Empate!'.upper()))
    elif jogador == 'PEDRA' and computador == 'PAPEL':
        print('\n{:-^35}'.format('Computador venceu!'.upper()))
    elif jogador == 'PEDRA' and computador == 'TESOURA':
        print('\n{:-^35}'.format('Você venceu!'.upper()))
    elif jogador == 'PAPEL' and computador == 'TESOURA':
        print('\n{:-^35}'.format('Computador venceu!'.upper()))
    elif jogador == 'PAPEL' and computador == 'PEDRA':
        print('\n{:-^35}'.format('Você venceu!'.upper()))
    elif jogador == 'TESOURA' and computador == 'PEDRA':
        print('\n{:-^35}'.format('Computador venceu!'.upper()))
    elif jogador == 'TESOURA' and computador == 'PAPEL':
        print('\n{:-^35}'.format('Você venceu!'.upper()))
    elif computador == 'PEDRA' and jogador == 'PAPEL':
        print('\n{:-^35}'.format('Você venceu!'.upper()))
    elif computador == 'PEDRA' and jogador == 'TESOURA':
        print('\n{:-^35}'.format('Computador venceu!'.upper()))
    elif computador == 'PAPEL' and jogador == 'TESOURA':
        print('\n{:-^35}'.format('Você venceu!'.upper()))
    elif computador == 'PAPEL' and jogador == 'PEDRA':
        print('\n{:-^35}'.format('Computador venceu!'.upper()))
    elif computador == 'TESOURA' and jogador == 'PEDRA':
        print('\n{:-^35}'.format('Você venceu!'.upper()))
    elif computador == 'TESOURA' and jogador == 'PAPEL':
        print('\n{:-^35}'.format('Computador venceu!'.upper()))
elif opção == 2:
    print('\n{:-^45}'.format('regras do jogo'.upper()))
    print('Pedra: ganha da tesoura e perde para o papel;')
    print('Papel: ganha da pedra e perde para a tesoura;')
    print('Tesoura: ganha do papel e perde para a pedra.')
    print('-----' * 9)
    start = input('\nComeçar? S/N ').upper()
    if start == 'S':
        print('--x--' * 7)
        print('{:^35}'.format(nome_jogo).upper())
        print('--x--' * 7)
        jogador = input('Qual sua escolha? ').upper()
        opções = ['PEDRA', 'PAPEL', 'TESOURA']
        computador = choice(opções).upper()
        print('--x--' * 7)
        sleep(0.5)
        print('{:^35}'.format('jo').upper())
        sleep(0.5)
        print('{:^35}'.format('ken').upper())
        sleep(0.5)
        print('{:^35}'.format('pô!').upper())
        sleep(0.5)
        print('-----' * 7)
        print('{:^35}'.format(nome_jogo).upper())
        print('-----' * 7)
        print('{:^35}\n'.format(título1))
        print('{:>12}'.format(jogador.upper()), end="    x    ")
        print('{}'.format(computador))
        if jogador == computador:
            print('\n{:-^34}'.format('Empate!'.upper()))
        elif jogador == 'PEDRA' and computador == 'PAPEL':
            print('\n{:-^35}'.format('Computador venceu!'.upper()))
        elif jogador == 'PEDRA' and computador == 'TESOURA':
            print('\n{:-^35}'.format('Você venceu!'.upper()))
        elif jogador == 'PAPEL' and computador == 'TESOURA':
            print('\n{:-^35}'.format('Computador venceu!'.upper()))
        elif jogador == 'PAPEL' and computador == 'PEDRA':
            print('\n{:-^35}'.format('Você venceu!'.upper()))
        elif jogador == 'TESOURA' and computador == 'PEDRA':
            print('\n{:-^35}'.format('Computador venceu!'.upper()))
        elif jogador == 'TESOURA' and computador == 'PAPEL':
            print('\n{:-^35}'.format('Você venceu!'.upper()))
        elif computador == 'PEDRA' and jogador == 'PAPEL':
            print('\n{:-^35}'.format('Você venceu!'.upper()))
        elif computador == 'PEDRA' and jogador == 'TESOURA':
            print('\n{:-^35}'.format('Computador venceu!'.upper()))
        elif computador == 'PAPEL' and jogador == 'TESOURA':
            print('\n{:-^35}'.format('Você venceu!'.upper()))
        elif computador == 'PAPEL' and jogador == 'PEDRA':
            print('\n{:-^35}'.format('Computador venceu!'.upper()))
        elif computador == 'TESOURA' and jogador == 'PEDRA':
            print('\n{:-^35}'.format('Você venceu!'.upper()))
        elif computador == 'TESOURA' and jogador == 'PAPEL':
            print('\n{:-^35}'.format('Computador venceu!'.upper()))
    else:
        print('Até mais!')
else:
    print('Até mais!')
    

