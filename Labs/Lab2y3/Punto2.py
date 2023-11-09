# Calculando el valor a pagar en una escuela de tenis

def _value_month(age,months):
    global category, value
    if age < 12:
        category = 'Infantil'
        value = months*43000
    elif age >= 12 and age < 18:
        category = 'Juvenil'
        value = months*36000
    else:
        category = 'Mayores'
        value = months*32000 
    return value
    
if __name__ == '__main__':
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    months = int(input('Enter your months: '))
    _value_month(age,months)
    print('\n')
    print('\tNombre: {}'.format(name))
    print('\tCategoria: {}'.format(category))
    print('\tValor a Pagar: {}'.format(value))