# Calcular el pago de empleados univalle
menu = '''\t\tWelcome
Let's go to calculate salary employes Univalle'''
salary = 1000000

def title():
    print('\n')
    for i in range(1,55):
        print('=', end = '')
    print('DATOS DEL EMPLEADO', end = '')
    for i in range(1,57):
        print('=', end = '')
    print('\n')

def title_p():
    print('\n')
    for i in range(1,62):
        print('=', end = '')
    print('PAGOS', end = '')
    for i in range(1,63):
        print('=', end = '')
    print('\n')

def title_d():
    print('\n')
    for i in range(1,60):
        print('=', end = '')
    print('DESCUENTOS', end = '')
    for i in range(1,60):
        print('=', end = '')
    print('\n')

def title_t():
    print('\n')
    for i in range(1,61):
        print('=', end = '')
    print('TOTALES', end = '')
    for i in range(1,62):
        print('=', end = '')
    print('\n')

if __name__ == '__main__':
    n = 1
    salary = 1000000
    name = 'San'
    id = '1023'
    
    print(menu)
    cant = int(input('Enter Number Employes: '))
    
    while(n < cant + 1):
        id = input("Enter your id: ")
        name = input('Enter your name: ')
        salary = int(input("Enter your basic salary: "))
        aux_trans = salary*(20/100)
        tip_service = salary*(10/100)
        
        total_add = aux_trans + tip_service

        health = salary*(4/100)
        tip_finally = salary*(4/100)
        tax = salary*(5/100)

        total_menos = health + tip_finally + tax

        total = salary + total_add - total_menos

        title()
        print('Name: {}'.format(name))
        print('id: {}'.format(id))

        title_p()
        print('Salary: {}'.format(salary))
        print('Tip of Service: {}'.format(tip_service))
        print('Tip for transportation: {}'.format(aux_trans))

        title_d()
        print('Health: {}'.format(health))
        print('Pension: {}'.format(tip_finally))
        print('Taxes: {}'.format(tax))

        title_t()
        print('Total Pagos: {}'.format(total_add))
        print('Total Descuentos: {}'.format(total_menos))
        print('Neto a Pagar: {}'.format(total))
        n += 1
        print('\n')