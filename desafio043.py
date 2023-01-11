from math import pow
print('\n   Calculadora de IMC'.upper())
print('--x--' * 5)
peso = float(input('Seu peso em Kg: '))
altura = float(input('Sua altura em m: '))
imc = peso / (pow(altura, 2))
print('--x--' * 5)
print('{:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')