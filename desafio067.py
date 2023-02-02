print('=-' * 11)
print('{:^22}'.format('Exibidor de tabuada'.upper()))
print('=-' * 11)
while True:
    tabuada = int(input('Tabuada desejada: '))
    print('=-' * 11)
    if tabuada < 0:
        print('\nEncerrando...')
        break
    print('')
    c = 1
    while c < 11:
        resultado = tabuada * c
        print('{} x {} = {}'.format(tabuada, c, resultado))
        c += 1
    print('')
    print('=-' * 11)
    