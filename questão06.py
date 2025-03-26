import random
num = random.randint(1, 9)
nn = input('Tente adivinhar o número de 1 a 9! ')
print('Digite sair se quiser sair')
while nn != str(num):
    if nn == 'sair':
        break
    if int(nn) > num:
        print('O número que você digitou é maior: ')
    elif int(nn) < num:
        print('O número que você digitou é menor')
    nn = input('Tente adivinhar o número novamente: ')
print('Finalizado')
print('Parabéns')
