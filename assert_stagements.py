def divisor(num):
    divisor = []
    for i in range (1, num+1):
        if num % i == 0:
            divisor.append(i)
    return divisor
        
        
def run():
    num = input('Ingresa un numero natural: ')

    assert num.isnumeric() and int(num) > 0, 'Debes ingresar un numero natural positivo'

    print(divisor(int(num)))
    print('termino mi programa')


if __name__ == '__main__':
    run()