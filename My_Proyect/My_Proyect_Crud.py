#   My Proyect CRUD = Crear, Leer, Actualizar, Eliminar
clients = 'Luis, Kevin, Santiago'

def create_client(new_client): # Función Crear
    global clients 
    if new_client not in clients: # Not in | Pregunta si el primer parametro no esta en el segundo
        clients += new_client
        get_list_client_names()
    else:
        print('The Client {} already exists'.format(new_client))

def read_client(search_client): # Función Leer
    global clients
    if search_client in clients:
        print('Client Exists')
    else:
        print('Client Not Exists')

def update_client(client_name,upd_client):  # Función Actualizar
    global clients
    clients = clients.replace(client_name,upd_client)
    
def delete_client(client_name, del_client): # Función Eliminar
    global clients
    if client_name in clients:
        clients = clients.replace(del_client,"")

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
    global clients
    print(clients)

def add_comma():    # Creamos una función para agregar "," y nos modifique la base de datos
    global clients
    clients += ", "

if __name__ == '__main__':
    welcome()
    option = input('\nType option desired client: ').upper()
    if option == 'C':
        client_name = get_name_client().capitalize()
        add_comma()
        create_client(client_name)
    elif option == 'R':
        client_name = get_name_client().capitalize()
        read_client(client_name)
        get_list_client_names()
    elif option == 'U':
        client_name = get_name_client().capitalize()
        if client_name in clients:
            upd_client = input('Name to Update: ').capitalize()
            update_client(client_name,upd_client)
            get_list_client_names()
        else:
            print('User no Exists')
    elif option == 'D':
        client_name = get_name_client().capitalize()
        if client_name in clients:
            del_client = input('Name to Delete: ').capitalize()
            if del_client in clients:
                delete_client(client_name,del_client)
            else:
                print('Clients no Exists')
            get_list_client_names()
        else:
            print('User no Exists')
    else:
        print('Command Invalid')