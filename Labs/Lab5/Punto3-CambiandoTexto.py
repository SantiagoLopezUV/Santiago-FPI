#   Cambiar cadena de texto por mayusculas
def change_fuente(phrase):
    words = phrase.split()
    word = []
    print(words)
    for i in words:
        word.append(i.capitalize())
    print(word)
    new = ' '.join(word)
    print(new)


if __name__ == '__main__':
    phrase = input("Enter Phrase: ")
    change_fuente(phrase)
    