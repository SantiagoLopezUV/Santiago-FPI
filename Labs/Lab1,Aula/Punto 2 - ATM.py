tarjetas = [
    {"numero": "1234567890", "clave": "1234", "saldo": 10000},
    {"numero": "0987654321", "clave": "4321", "saldo": 5000},
    {"numero": "5678901234", "clave": "5678", "saldo": 20000}
]

card = input("Enter Number of Card: ")
print("Reading.....")
for tarjeta in tarjetas:
    n_card = tarjeta['numero']
    if card in n_card:
        password = input("Enter Password: ")
        if password == tarjeta['clave']:
            if tarjeta['saldo'] >= 10000:
                cash = int(input('Enter the amount.: '))
                if cash <= tarjeta['saldo']:
                    print("\n...Count money...\n")
                    print("\tWithdraw the money")
                else:
                    print("I'm sorry. I don't have enough money")
                    break
            else:
                print("I'm Sorry, You don't Have money")
                break
        else:
            print('Password Incorrect')
            break
    else:
        continue
if n_card == card:
    print("Thanks you")
else:
    print("Oh, Card Incorrect")
