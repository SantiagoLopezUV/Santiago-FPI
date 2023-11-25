# Contar caracteres de una frase

abc = 'ABCDEFGHIJKLMNOPQRSTVWXYZ'
vocal = "aeiouáéíóúAEIOUÁÉÍÓÚ"

def fun(frase):
    small_word = 0
    mayus = 0
    vocals = 0
    text = frase.split()
    print(text)
    for word in text:
        if len(word) < 3:
            small_word += 1
        for i in word:
            if i in abc:
                mayus += 1
            if i in vocal:
                vocals += 1
    print("The number of words with less than 3 letters: {}".\
        format(small_word))
    print("The number of letters in size MAX: {}".format(mayus))
    print("The number of letters vocals: {}".format(vocals))


if __name__ == '__main__':
    frase = input("Enter Phrase: ")
    fun(frase)
