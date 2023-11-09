# Calculando el valor cualitativo
# Un Examen Parcial 20%
# Examen Final  40%
# Tareas    20%
# Participación 20%

menu = 'Hi! Lets go make to informe'

def list_courses():
    print('1: Fundamentos\n2: Calculo I')
    print('3: Ingles I\n4: Deporte')

def get_courses(course):
    global materia
    global conta
    if course == 1:
        materia = 'Fundamentos'
        conta = 1
    elif course == 2:
        materia = 'Calculo I'
        conta = 2
    elif course == 3:
        materia = 'Ingles I'
        conta = 3
    elif course == 4:
        materia = 'Deporte'
        conta = 4
    else:
        print('Option Incorrect')

def note_definitive(parcial, final, homew1, homew2, parti):
    note = (parcial*(20/100) 
            + final*(40/100)
            + homew1*(20/100)
            + homew2*(20/100)
            + parti/10)
    if note >= 5:
        note = 4.9
    return note

def calification(num_signature, definitive):
    if num_signature == 'FUNDAMENTOS':
        if definitive >= 0 and definitive < 2:
            return 'Malo'
        elif definitive >= 2 and definitive < 3:
            return 'Deficiente'
        elif definitive >= 3 and definitive < 3.8:
            return 'Regular'
        elif definitive >= 3.8 and definitive < 4.5:
            return 'Bueno'
        elif definitive >= 4.5 and definitive < 5:
            return 'Excelente'
        else:
            return 'ERROR NOTE'
    elif num_signature == 'CALCULO':
        if definitive >= 0 and definitive < 2:
            return 'Malo'
        elif definitive >= 2 and definitive < 3:
            return 'Deficiente'
        elif definitive >= 3 and definitive < 3.5:
            return 'Regular'
        elif definitive >= 3.5 and definitive < 4.5:
            return 'Bueno'
        elif definitive >= 4.5 and definitive < 5:
            return 'Excelente'
        else:
            return 'ERROR NOTE'
    elif num_signature == 'INGLES':
        if definitive >= 0 and definitive < 3:
            return 'Deficiente'
        elif definitive >= 3 and definitive < 4:
            return 'Regular'
        elif definitive >= 4 and definitive < 4.5:
            return 'Bueno'
        elif definitive >= 4.5 and definitive < 5:
            return 'Excelente'
        else:
            return 'ERROR NOTE'
    elif num_signature == 'DEPORTE':
        if definitive >= 0 and definitive < 3:
            return 'Malo'
        elif definitive >= 3 and definitive < 4:
            return 'Regular'
        elif definitive >= 4 and definitive < 5:
            return 'Bueno'
        else:
            return 'ERROR NOTE'

if __name__ == '__main__':
    print(menu)
    name = input('Enter your Name: ')
    num_signature = input('Enter your Signature: ').upper()
    parcial = float(input('Enter your note of Parcial: '))
    final = float(input("Enter your note of Final: "))
    homew1 = float(input("Enter your note of Homework 1: "))
    homew2 = float(input("Enter your note of Homework 2: "))
    parti = float(input("Enter your note of Participate: "))
    definitive = note_definitive(parcial, final, homew1, homew2, parti)
    clasif_note = calification(num_signature, definitive)
    print('Name of the Student: {}'.format(name))
    print('Name of the Signature: {}'.format(num_signature))
    print('Clasification from note: {}'.format(clasif_note))
