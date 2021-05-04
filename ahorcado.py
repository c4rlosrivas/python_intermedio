
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

def run():
    a = read_data()
    word = choose_word(a)
    print(word)

if __name__ == '__main__':
    run()