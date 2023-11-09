menu = """Welcome to Censo Virtual"""
def title(a):
    for i in range(0, 50):
        print('=', end = "")
    if a == 0:
        print('BOSS OF THE HOME', end = "")
    else:
        print('    FAMILIER    ', end = "")
    for i in range(0, 50):
        print('=', end = "")
    print('\n')

def _boss_user():
    global number_family
    title(a = 0)
    name = input('Enter your name: ')
    last_name = input('Enter your last name: ')
    type_id = input('Enter your type of id: ')
    id = input('Enter your id: ')   
    fecha = input('Enter Fecha Nacimiento: ')
    estate = input('Enter your estate: ')
    city = input('Enter your city: ')
    adress = input('Enter your adress: ')
    number_family = int(input("Enter number of family to register: "))
    return name, last_name, type_id, id, fecha, estate, city, adress

def _get_user():
    title(a = 1)
    _name_ = input('Enter Name: ')
    __lastname_ = input('Enter lastname: ')
    _type_id_ = input('Enter type id: ')
    _id_ = input('Enter id: ')
    _fecha_ = input('fecha nacimiento: ')
    family = input('type familier: ')
    return _name_, __lastname_, _type_id_, _id_, _fecha_, family

if __name__ == '__main__':
    _boss_user()
    print('\n')
    for i in range(1, number_family + 1):
        _get_user()