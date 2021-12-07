#The challenge is build any decorator

def only_send_numbers(func):
    def wrapper():
        iterable = int(input('Ingrese la cantidad de números a ingresar: '))
        send_list = []
        for i in range(0, iterable):
            try:
                number = input('Ingrese un número: ')
                send_list.append(int(number))
            except ValueError:
                print(f'Error "{number}" is not a number')

        print('\nEnviando solo números')
        func(send_list)
        print('Hecho\n')
    return wrapper


@only_send_numbers
def an_operation(lis):
    sum = 0
    for i in lis:
        sum += i
    print(sum)


@only_send_numbers
def multip(lis):
    mul = 1
    for i in lis:
        if i > 0:
            mul *= i
    print(mul)

an_operation()
multip()