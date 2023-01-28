número = int(input('Fatorial desejado: '))
fatorial = 1
c = 1
while c < número+1:
    fatorial = fatorial * c
    c += 1
print('{}! é igual a {}.'.format(número, fatorial))
