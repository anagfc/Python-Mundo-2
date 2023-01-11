print('Analisador de triângulos'.upper())
l1 = float(input('Insira o 1º lado do triângulo: '))
l2 = float(input('Insira o 2º lado do triângulo: '))
l3 = float(input('Insira o 3º lado do triângulo: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('Essas medidas formam um triângulo.')
else:
    print('Essas medidas NÃO formam um triângulo.')

if l1 != l2 != l3:
    print('Seu triângulo é escaleno.')
elif l1 == l2 == l3:
    print('Seu triângulo é equilátero.')
else:
    print('Seu triêngulo é isóceles.')
    