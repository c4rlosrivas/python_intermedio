def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname': 'Carlos', 'lastname': 'Rivas'}

    super_list = [
        {'firstname': 'Carlos', 'lastname': 'Rivas'},
        {'firstname': 'Cabezas', 'lastname': 'Cabazas'},
        {'firstname': 'Victor', 'lastname': 'Pantoja'},
        {'firstname': 'Gabriel', 'lastname': 'Moran'},
        {'firstname': 'Allisson', 'lastname': 'Morales'}
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1.1, 4.5, 6.43]
    }

    print('Listas dentro de dicionarios')
    for key, value in super_dict.items():
        print(key, '-', value)

    print('Diccionarios dentro de listas')
    #usando ciclo for
    for i in super_list:  
        print(i['firstname'], i['lastname'])

    #usando ciclo while
    # i = 0
    # while i < len(super_list):
    #     info = super_list[i]
    #     print(info['firstname'], info['lastname'])
    #     i = i+1
        

if __name__ == '__main__':
    run()