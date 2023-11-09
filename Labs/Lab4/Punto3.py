# AciertoMultiplicacion

import random


def product_lucky(number_1, number_2):
    global conta
    global conta2
    product = number_1 * number_2
    try:
        n = int(input('Cual es el Producto de {} * {}: '.format(number_1, number_2)))
    except ValueError:
        return 'Error, Just Numbers'
    else:
        if n == product:
            print('Acertaste!')
            conta += 1
        else:
            print('ERROR, Correct is {}'.format(product))
            conta2 += 1
        return product

if __name__ == '__main__':
    conta = 0
    conta2 = 0
    name = input('Enter Your Name: ')
    for i in range(1, 13):
        number_1 = random.randint(-5,15)
        number_2 = random.randint(-5,15)
        n = product_lucky(number_1, number_2)
        print(n)
    print('{}, Buenas {} y Malas {}'.format(name, conta, conta2))

