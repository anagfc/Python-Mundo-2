frase = str(input('Insira uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
'''Em Python é possível substituir esse modo de inverter a frase por inverso = junto[::-1] (vai do início ao fim, ao contrário) '''

if junto == inverso:
    print('{} invertido é {}. Sua frase é palíndroma!'.format(junto, inverso))
else:
    print('{} invertido é {}. Sua frase não é palíndroma.'.format(junto, inverso))
    