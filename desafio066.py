soma = quantidade = 0
while True:
    número = int(input('Insira um valor inteiro [999 para a execução]: '))
    if número == 999:
        break
    soma += número
    quantidade += 1
print(f'Você inseriu {quantidade} valores que, somados, resultam em {soma}.')
