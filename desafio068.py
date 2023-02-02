from random import randint
vitória = 0
while True:
    print('-+-' * 8)
    print('{:^24}'.format('Par ou ímpar'.upper()))
    print('-+-' * 8)
    print('{:^24}'.format('Você'))
    jogador_classe = input('Par ou ímpar? [P/I]: ').upper().strip()
    while jogador_classe != 'P' and jogador_classe != 'I':
        jogador_classe = input('Par ou ímpar? [P/I]: ').upper().strip()
    jogador_número = int(input('Sua jogada: '))
    print('-' * 24)
    computador = randint(0, 10)
    resultado = computador + jogador_número
    print('{:^24}'.format('Computador'))
    print('Par' if jogador_classe == 'I' else 'Ímpar')
    print(f'Jogada: {computador}')
    print('-' * 24)
    print('{:^24}'.format('Resultado'.upper()))
    print(f'Soma dos valores: {resultado}')
    if jogador_classe == 'P' and resultado % 2 == 0:
        print('\033[32mParabéns! Você venceu.\033[m\n')
        vitória += 1
    elif jogador_classe == 'I' and resultado % 2 != 0:
        print('\033[32mParabéns! Você venceu.\033[m\n')
        vitória += 1
    else:
        print(f'\033[31mVocê perdeu.\033[m\nVitórias consecutivas: {vitória}')
        break
