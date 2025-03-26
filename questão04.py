while True:
    print(' ')
    print('Digite 0 para sair')
    nn = int(input('Digite um número: '))
    if nn == 0:
        break
    divisor = 1
    while divisor <= nn:
        if nn % divisor == 0:
            print(divisor)
        divisor += 1