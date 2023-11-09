#   Algoritmos con estructuras de repeticion

def numeros_pares(a):   # Los 50 Numeros pares
    n = 1
    for i in range(a*2):
        if n%2 == 0:
            print(n)
            n += 1
        else:
            n += 1

def multiplos_7(a):  # Los 100 primeros numeros multiplos de 7
    n = 1
    conta = 1
    for i in range(1, (a+1)*7):
        if n%7 == 0:
            print(n)
            conta += 1
            n += 1
        else:
            n += 1

def numeros_primos(a):  #Numeros primos menores que 30
    n = 1
    for i in range(1,a):
        if n % 2 == 0 or n % 3 == 0 or n % 4 == 0 or n % 5 == 0:
            n += 1
        elif n==1:
            n += 1
        else:
            print(n)
            n += 1

if __name__ == '__main__':
    numeros_primos(30)
