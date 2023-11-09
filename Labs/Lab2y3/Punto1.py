#   Calculando el indice de masa corporal IMC

def category_imc(weight,height):
    global cat, imc
    imc = weight/(height**2)
    if imc < 18.5:
        cat = 'Infrapeso'        
    elif imc >= 18.5 and imc < 25:
        cat = 'Normal'
    else:
        cat = 'Sobrepeso'

if __name__ == '__main__':
    name = input('Enter your name: ')
    weight = float(input('Enter your weight: ')) #Peso
    height = float(input('Enter your height: ')) #Altura
    category_imc(weight,height)
    print('\n')
    print('\tPACIENTE: {}'.format(name))
    print('\tIMC: {}'.format(imc))
    print('\tCategoria: {}'.format(cat))