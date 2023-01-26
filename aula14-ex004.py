n = 1
par = 0
ímpar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: # Para não analisar o zero que finaliza o programa
        if n % 2 == 0:
            par += 1
        else:
            ímpar += 1
print('Você digitou {} valores pares e {} valores ímpares.'.format(par, ímpar))