import random
recebimento = input('voc� gosta de jogar dados? ').lower()
if recebimento == 'sim':
    print('eu tamb�m')
    lado = str(input('quantos lados do dado voc� vai querer, de 3, de 6, de 8, de 10, de 12, de 24 ou 100? '))
    if lado == '3':
        print(random.randrange(1, 3))
    elif lado == '6':
        print(random.randrange(1, 6))
    elif lado == '8':
        print(random.randrange(1, 8))
    elif lado == '10':
        print(random.randrange(1, 10))
    elif lado == '12':
        print(random.randrange(1, 12))
    elif lado == '24':
        print(random.randrange(1, 24))
    elif lado == '100':
        print(random.randrange(1, 100))
    else:
        print('voc� deve escolher um dos numeros \'3, 6, 8, 10, 12, 24 e 100\' ')
elif recebimento == 'n�o':
    print('que pena, queria jogar com voc�')
else:
    print('voc� s� pode colocar \'sim\' ou \'n�o\' ')