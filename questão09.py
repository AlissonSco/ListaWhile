nn = int(input('Digite um numero: '))
numero = nn
qntdDigitos = 0

while numero > 0:
    numero = numero // 10
    qntdDigitos = qntdDigitos + 1
soma = 0
numero = nn

while numero > 0:
    digito = numero % 10
    soma = soma + (digito ** qntdDigitos)
    numero = numero // 10

if soma == nn:
    print('O numero é um numero de armstrong.')
else:
    print('O numero nao é um numero de armstrong.')