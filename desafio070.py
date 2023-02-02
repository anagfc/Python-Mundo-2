valor_compra = caros = barato = 0
item_barato = ''
print('{:^30}'.format('Lista de compras').upper())
print('-' * 30)
while True:
    item = input('Nome do item: ').capitalize()
    valor_un = float(input('Valor unitário: R$'))
    quantidade = int(input('Quantidade: '))
    valor_item = valor_un * quantidade
    valor_compra += valor_item
    if valor_un >= 1000:
        caros += 1
    if barato == 0:
        barato = valor_un
    if barato > valor_un:
        barato = valor_un
        item_barato = item
    print('-' * 30)
    novo = input('Cadastrar novo item? [S/N] ').upper()
    print('-' * 30)
    if novo == 'N':
        break
print('-' * 30)
print('Total da compra: R${:.2f}'.format(valor_compra))
print('{} itens comprados custam mais de R$1.000,00.'.format(caros))
print('O item mais barato comprado foi {}, com valor unitário de R${:.2f}.'.format(item_barato, barato))
