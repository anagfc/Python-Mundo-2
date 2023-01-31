print('-' * 35)
print('{:^35}' .format('Sequência de Fibonacci'))
print('-' * 35)
elementos = int(input('Quantos elementos deseja exibir? '))
print('\n')
c = 1
anterior = 0
atual = 0
próximo = 0
while c < elementos+1:
    print(próximo, end = '... ')
    if c == 1:
        próximo += 1
    anterior = atual
    atual = próximo
    próximo = anterior + atual
    c += 1