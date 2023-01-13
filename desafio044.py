print('-x-' * 10)
print('    Condições de pagamento'.upper())
print('-x-' * 10)
preço = float(input('Preço do produto: R$'))
print('\nFormas de pagamento:')
print('1- À vista (dinheiro/cheque)')
print('2- À vista (cartão)')
print('3- Parcelado no cartão')
opção = int(input('Selecione uma opção: '))
if opção == 1:
    pagamento = preço - preço * 10 / 100
    print('Valor a ser pago: R${}.'.format(pagamento))
elif opção == 2:
    pagamento = preço - preço * 5 / 100
elif opção == 3:
    print('A- 2 parcelas (sem juros)')
    print('B- 3 parcelas ou mais')
    opção2 = (input('Selecione uma condição: ')).upper()
    if opção2 == 'A':
        print('Valor total: R${:.2f}.'.format(preço))
        print('Valor da prestação: 2x R${:.2f}.'.format(preço/2))
    else:
        pagamento = preço + preço * 20 / 100
        parcelas = int(input('Quantidade de parcelas: '))
        print('Valor total: R${:.2f}.'.format(pagamento))
        print('Valor da prestação: {}x R${:.2f}.'.format(parcelas, (pagamento/parcelas)))
else:
    print('Opção de pagamento inválida. Tente novamente.')
