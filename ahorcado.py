
#aqui va ir el juego del ahorcado
import random

def read_data():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n", "") #elimina salto de linea "\n"
            words.append(line)
    
    return(words)


def choose_word(word_list):
    len_list = len(word_list)
    k = random.randint(0, len_list-1)
    word_choosed = word_list[k]
    return(word_choosed)


def input_letter():
    try:
        letter = input("Ingresa una letra: ")

        if letter.isnumeric() == True or len(letter) > 1:
            raise ValueError("No ingresar numeros ni espacios")
        return letter
    
    except ValueError as ve:
        print(ve)
        return False


def letter_compared(original, new, new_word):  
    if new in original:  #detecta si la letra ingresada esta en la palabra
        i = 0
        while i < len(original):  #ubica la letra ingresada en la palabra nueva
            if new == original[i]:
                new_word[i] = new
            i = i+1
        return new_word
    else:
        print('Buen intento')
        return new_word


def run():
    a = read_data()
    word = choose_word(a)
    secret_word = [i for i in word]
    print(secret_word)
    
    if ('á' in secret_word) or ('é' in secret_word) or ('í'in secret_word) or ('ó'in secret_word) or ('ú' in secret_word):
        print('En la palabra hay una tilde')

    b = len(secret_word)
    
    i = 0
    new_list = ['' for i in range(0,b)]
    print(new_list)
    while i <= b:
        new_letter = input_letter()
        if new_letter !=False:
            new_list = letter_compared(secret_word, new_letter, new_list)
            i = i+1
            
            print(new_list)
    
            if not '' in new_list:
                print('ganaste')
                break 
    
if __name__ == '__main__':
    run()