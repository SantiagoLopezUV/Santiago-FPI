#   My Proyect CRUD = Crear, Leer, Actualizar, Eliminar
clients = {
    1: 'Luis',
    2: 'Kevin',
    3: 'Santiago'
    }

def create_client(new_client): # Función Crear
    if new_client not in clients.values():
        clients.setdefault(len(clients) + 1, new_client)
        #clients[len(clients)+1] = new_client
        get_list_client_names()
    else:
        print('The Client {} already exists'.format(new_client))


def read_client(search_client): # Función Leer
    if search_client in clients.values():
        print(clients.keys())
        for i in range(0,len(clients)):
            print('The Client {}: is {}'.format((i+1),\
                clients.get(i+1)))
    else:
        print("You don't have access")


def update_client(client_name):  # Función Actualizar
    if client_name in clients.values():
        while(True):
            upd_client = input('Name to Update: ').capitalize()
            if upd_client in clients.values():
                print('Client Exists')
            else:
                for keys, values in clients.items():
                    if values == client_name:
                        clients[keys] = upd_client
                        break
                    else:
                        continue
                get_list_client_names()
                break
    else:
        print("You don't have access")


def delete_client(client_name): # Función Eliminar
    if client_name in clients.values():
        while(True):
            del_client = input('Name to Delete: ').capitalize()
            if del_client in clients.values():
                for keys, values in clients.items():
                    if values == del_client:
                        clients.pop(keys)
                        break
                    else:
                        continue
                get_list_client_names()
                break
            else:
                print('Clients no Exists')
                get_list_client_names()
    else:
        print("You don't have access")


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