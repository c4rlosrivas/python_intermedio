def divisor(num):
    try:
        if num < 0:
            raise ValueError("Debes ingresar un entero positivo")
        
        divisor = []
        for i in range (1, num+1):
            if num % i == 0:
                divisor.append(i)
        return divisor
    
    except ValueError as ve:
        print(ve)
        return False
        
        
def run():
    try:
        num = int(input('Ingresa un numero natural: '))
        lista = divisor(num)
        if lista != False:
            print(lista)
            print('termino mi programa')
    except ValueError:
        print('Debes ingresar un numero')

if __name__ == '__main__':
    run()