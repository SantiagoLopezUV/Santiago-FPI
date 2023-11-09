# Calculando el Valor de una función
def funcion_x(x):
    global a
    if x <= 0:
        a = 8*(x**2)-6
    else:
        a = 3*x + 5
    return a
    
if __name__ == '__main__':
    x = int(input('Enter el value of X: '))
    funcion_x(x)
    print('f({}) = {}'.format(x,a))