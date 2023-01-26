soma = 0
valor_par = 0
for c in range(0, 6):
    num = int(input('Insira um valor: '))
    if num % 2 == 0:
        valor_par += 1
        soma += num
print('Você inseriu {} valores pares que, somados, equivalem a {}.'.format(valor_par, soma))
