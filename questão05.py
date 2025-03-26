nn = int(input('Digite um numero: '))
nn2 = 0

while nn > 0:
    nn2 = nn2 * 10 + nn % 10
    nn = nn // 10
    
print(f'Número invertido: {nn2}')