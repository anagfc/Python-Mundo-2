from random import randint
from time import sleep
computador = randint(0, 10)
tentativas = 1
print('\n')
print('=' * 25)
print('{:^25}'.format('Adivinhe o número').upper())
print('=' * 25)
print('[1] Começar\n[2] Instruções\n[3] Sair')
opção = int(input('Selecione uma opção: '))
if opção == 1:
    print('\n')
    print('=' * 25)
    print('O computador está pensando em um número...')
    sleep(0.5)
    print('Pronto!')
    jogador = int(input('Em qual número o computador pensou? '))
    if jogador == computador:
        print('{:^25}'.format('Parabéns!'.upper()))
        print('Você acertou na {}ª tentativa!'.format(tentativas))
    while jogador != computador:
        print('\nAinda não foi dessa vez! Tente de novo.')
        tentativas += 1
        jogador = int(input('Em qual número o computador pensou? '))
    print('-' * 25)
    print('{:^25}'.format('Parabéns!'.upper()))
    print('Você acertou na {}ª tentativa!'.format(tentativas))
elif opção == 2:
    print('\n')
    print('=' * 25)
    print('{:^25}'.format('Instruções'.upper()))
    print('=' * 25)
    print('O Computador irá pensar\nem um número inteiro que\nfique entre 0 e 10. Sua\ntarefa é descobrir qual\no número no menor número\nde tentativas possíveis.\n')
    print('=' * 25)
    print('\n')
    print('=' * 25)
    print('{:^25}'.format('Adivinhe o número').upper())
    print('=' * 25)
    print('[1] Começar\n[2] Sair')
    opção2 = int(input('Selecione uma opção: '))
    if opção2 == 1:
        print('\n')
        print('=' * 25)
        print('O computador está pensando em um número...')
        sleep(0.5)
        print('Pronto!')
        jogador = int(input('Em qual número o computador pensou? '))
        if jogador == computador:
            print('{:^25}'.format('Parabéns!'.upper()))
            print('Você acertou na {}ª tentativa!'.format(tentativas))
        while jogador != computador:
            print('\nAinda não foi dessa vez! Tente de novo.')
            tentativas += 1
            jogador = int(input('Em qual número o computador pensou? '))
        print('-' * 25)
        print('{:^25}'.format('Parabéns!'.upper()))
        print('Você acertou na {}ª tentativa!'.format(tentativas))
    else:
        print('Até mais!')
else:
    print('Até mais!')