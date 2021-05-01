def run():
    # lista de numeros no divisibles a 3

    # modo tradicional
    # squared = []
    # for num in range(1, 101):
    #     if (num%3) != 0:
    #         squared.append(num**2)

    #nuevo metodo
    # squared = [i**2 for i in range(1, 101) if i%3 != 0]

    # print(squared)

    lista = [i for i in range(1, 100000) if i%4 == 0 and  i%6 == 0 and i%9 ==0]
    print(lista)

if __name__ == '__main__':
    run()