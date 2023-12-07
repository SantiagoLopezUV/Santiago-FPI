from tabulate import tabulate

matriz =[]


def create_matriz():
    for i in range(10):
        route = input("Enter Route {}: ".format(i+1))
        matriz.append([route])
        passenger = input("Enter Number Passenger on route {}: ".format(i+1))
        matriz[i].append(passenger)
    print(tabulate(matriz))
    col = len(matriz[0])
    return col


def count_passenger(col):
    num = 0
    count = []
    for i in range(1, col):
        for j in matriz:
            num += j[i]
            count.append(j[i])
    maxim = max(count)
    route = index_route(maxim)
    print("The route with Maxim of passenger is: {} - {}"\
        .format(route, maxim))
    print("The Number of Passenger of a day is: {}".format(num))


def index_route(maxim):
    for k in matriz:
        for l in k:
            if l == maxim:
                route = k[0]
                return route


if __name__ == '__main__':
    column = create_matriz()
    print(tabulate(matriz))
    count_passenger(column)
