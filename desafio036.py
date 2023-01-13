print('\033[33m--=--'*20)
print('                                Consulta de empréstimo imobiliário'.upper())
print('--=--'*20)
nome = input('\033[mNome completo do comprador: ')
nomef = nome.split()
print('\nOlá, {}. Seja bem-vindo à sua simulação de empréstimo.'.format(nomef[0].title()))
preço = float(input('\nValor do imóvel: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Em quantos anos pretende pagar: '))

prestação = preço / (anos * 12)
print('\n')
print('-=*=-'*20)
print('                                Comprador: {}'.format(nome.title()))
if prestação > salário * 30 / 100:
    print('\n\033[31mSituação: empréstimo NEGADO\033[m')
    print('Prestação mensal excede R${:.2f} (30% da renda)\n'.format(salário * 30 / 100))
else:
    print('\n\033[32mSituação: empréstimo APROVADO\033[m')
    print('Valor mensal das prestações: R${:.2f}.'.format(prestação))
    print('Prazo de pagamento: {} meses\n'.format(anos * 12))
print('-=*=-'*20)