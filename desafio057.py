sexo = input('Insira seu sexo [F/M]: ').upper().strip()
while sexo != 'F' and sexo != 'M': #While sexo not in 'MmFf':
    print('Resposta inválida.')
    sexo = input('Insira seu sexo [F/M]: ').upper()
