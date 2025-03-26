binario = int(input('Digite um numero binario: '))
decimal = 0
i = 0

while binario > 0:
    digito = binario % 10
    decimal = decimal + (digito * (2 ** i))
    binario = binario // 10
    i = i + 1
    
print(f'O numero decimal e: {decimal}')