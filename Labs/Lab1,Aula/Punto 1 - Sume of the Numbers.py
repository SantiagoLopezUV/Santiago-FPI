# Sume of the Numbers

import random

n = random.randint(10000,99999)

print(n)
conta = 0
lista = []

for i in str(n):
    lista.append(i)
    conta += 1

suma_1 = int(lista[0]) + int(lista[1]) + int(lista[2])
suma_2 = int(lista[-1]) + int(lista[-2])

print("The sum of the first 3 numbers is: {}".format(suma_1))
print("The sum of the first 2 numbers is: {}".format(suma_2))
if suma_1 != suma_2:
    print('Verification Incorrect')
else:
    print("Verification is Correct")
print('The number of digits is: {}'.format(conta))
print("Number: {}".format(n))