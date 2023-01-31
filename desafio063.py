print('-' * 35)
print('{:^35}' .format('Sequência de Fibonacci'))
print('-' * 35)
elementos = int(input('Quantos elementos deseja exibir? '))
print('\n')
c = 1
anterior = 0
atual = 0
próximo = 1
print(atual, end = '... ')
while c < elementos:
    print(próximo, end = '... ')
    anterior = atual
    atual = próximo
    próximo = anterior + atual
    c += 1
    