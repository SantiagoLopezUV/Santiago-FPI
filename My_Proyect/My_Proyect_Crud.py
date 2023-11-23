#   My Proyect CRUD = Crear, Leer, Actualizar, Eliminar
clients = ['Luis', 'Kevin', 'Santiago']

def create_client(new_client): # Función Crear
    if new_client not in clients: # Not in | Pregunta si el primer parametro no esta en el segundo
        clients.append(new_client)
        get_list_client_names()
    else:
        print('The Client {} already exists'.format(new_client))


def read_client(search_client): # Función Leer
    for search, client in enumerate(clients, 1):
        print('{}: {}'.format(search, client))


def update_client(client_name):  # Función Actualizar
    if client_name in clients:
        while(True):
            upd_client = input('Name to Update: ').capitalize()
            if upd_client in clients:
                print('Client Exists')
            else:
                index = clients.index(client_name)
                clients[index] = upd_client
                get_list_client_names()
                break
    else:
        print('Client Not Exists')


def delete_client(client_name): # Función Eliminar
    if client_name in clients:
        while(True):
            del_client = input('Name to Delete: ').capitalize()
            if del_client in clients:
                clients.remove(del_client)
                get_list_client_names()
                break
            else:
                print('Clients no Exists')
                get_list_client_names()


def welcome():  # Presentación del Programa
    print('\n\t\t\t\t\tWELCOME TO UNIVERSITY DEL VALLE - COL')
    print('*' * 128)
    print('What would you like to do today: ')
    print('[C]reate Client o User: ')
    print('[R]ead Client o User: ')
    print('[U]pdate Client o User: ')
    print('[D]elate Client o User: ')


def get_name_client():  # Creamos una función que permite preguntar nombre cliente
    return input("Enter your name: ")


def get_list_client_names():    # Creamos una función que nos imprima la base de datos
    print(clients)


def add_comma():    # Creamos una función para agregar "," y nos modifique la base de datos
    global clients
    clients += ", "


if __name__ == '__main__':
    welcome()
    option = input('\nType option desired client: ').upper()
    if option == 'C':
        client_name = get_name_client().capitalize()
        create_client(client_name)
    elif option == 'R':
        client_name = get_name_client().capitalize()
        read_client(client_name)
    elif option == 'U':
        client_name = get_name_client().capitalize()
        update_client(client_name)
    elif option == 'D':
        client_name = get_name_client().capitalize()
        delete_client(client_name)
    else:
        print('Command Invalid')