def run():
    # my_dict = {}

    # for i in range(1,101):
    #     if i%3 != 0:
    #         my_dict[i] = i**3

    # print(my_dict)

    #aplicando dictionary comprehensions

    # my_dict = {i: i**3 for i in range(1,101) if i%3 != 0}
    # print(my_dict)

    dictionary = {i:round(i**0.5, 3) for i in range(1,1001)}
    print(dictionary)

if __name__ == '__main__':
    run()