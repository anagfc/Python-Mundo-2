soma = 0
for c in range(0, 6):
    num = int(input('Insira um valor: '))
    if num % 2 == 0:
        soma += num
print('Os valores pares somados equivalem a {}.'.format(soma))