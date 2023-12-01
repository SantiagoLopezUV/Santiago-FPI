import tabulate as tb 

#   Punto 1
employees = []

menu = """
    WELCOME TO COMPANY MY FUTURE
    """


def n_employ():
    while(True):
        try:
            n = int(input("Enter Number of employes: "))
            return n
        except ValueError:
            print("Enter Number of employes in Numbers")


def n_week():
    while(True):
        try:
            m = int(input("Enter Number of Weeks Worked: "))
            return m
        except ValueError:
            print("Enter Number of employes in Numbers")


def get_hour(j):
    while(True):
        try:
            hour = int(input("Enter number of hours worked in the week {}: ".format(j+1)))
            return hour
        except ValueError:
            print("Enter Number Int")


def add_hour(n, m):
    for i in range(n):
        employees.append([])
        name = input("\nEnter the name of the Employee {}: ".format(i+1)).capitalize()
        for j in range(m):
            if j == 0:
                employees[i].append(name)
            print(employees)
            hour = get_hour(j)
            employees[i].append(hour)


def salary_employee():
    valor = 0
    for employ in employees:
        for hour in employ:
            try:
                if hour >= 0:
                    valor += (hour * 10000)
            except TypeError:
                continue
        print("The Salary of employe {} is: {}".format(employ[0], valor))


def cost_company():
    print("Pays for the week")
    columnas = len(employees[0]) # Guardamos el Valor de la cantidad de elementos
    valor = 0
    for col in range(1, columnas):  # Iteramos sobre la cantidad de elementos
        for fila in employees:  # Iteramos en la Matriz toda la fila
            valor += fila[col]*10000    # En la primera posicion de la fila operamos
        print("On the week {} the value of pays is: {}".format(col, valor))


def main():
    n = n_employ()
    m = n_week()
    add_hour(n, m)
    print(tb.tabulate(employees))
    try:
        while(True):
            option = int(input("Select Option: "))
            if option > 0 and option <= 2:
                break
            else:
                print("Option Incorrect")
        if option == 1:
            salary_employee()
        if option == 2:
            cost_company()
    except ValueError:
        print("Select Option Correct")


if __name__ == '__main__':
    print(menu)
    main()
