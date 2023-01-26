divisões = 0 
num = int(input('Insira um número: '))
for c in range (1, num+1):
    if num % c == 0:
        print('\033[1;32m{}\033[m'.format(c), end = ' ')
        divisões += 1
    else:
        print('\033[31m{}\033[m'.format(c), end = ' ')
if divisões == 2:
    print('\nO número {} é um número primo, pois tem {} divisores.'.format(num, divisões))
else:
    print('\nO número {} não é um número primo, pois tem {} divisores.'.format(num, divisões))
    