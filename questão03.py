cont = 0
while True:
    print(' ')
    print('Se quiser sair digite 0')
    nn = int(input('Digite um numero: '))
    if nn == 0:
        break
    
    cont = cont+ nn
print(f'A soma dos numeros digitados é {cont}')