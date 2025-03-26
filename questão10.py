nn = int(input('Digite um numero: '))
numero = 1

while numero <= nn:
    n = numero
    qntdDigitos = 0

    while n > 0:
        n = n // 10
        qntdDigitos = qntdDigitos + 1
    soma = 0
    n = numero

    while n > 0:
        digito = n % 10
        soma = soma + (digito ** qntdDigitos)
        n = n // 10

    if soma == numero:
        print(f'{numero} e um numero de Armstrong.')
    numero = numero + 1