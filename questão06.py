import random
num = random.randint(1,9)
nn = int(input('Tente adivinhar o numero de 1 a 9! '))
print('Digite sair se quiser sair')
while nn != num:
    if nn > num:
        print('O numero que voce digitou e maior: ')
        nn = int('Tente adivinhar o numero novamente: ')
    elif nn < num:
        print('O numero que voce digitou e menor')
        nn = int(input('Tente adivinhar o numero novamente: '))
    else:
        print('FIM DO JOGO')
print('Parabéns')