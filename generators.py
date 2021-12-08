from time import sleep
#A better way to build a iterator
from typing import Counter

def fibo_gen(max = 10):
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        elif counter >= max:
            break
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux


if __name__ == '__main__':
    fibonacci = fibo_gen(15)
    for element in fibonacci:
        print(element)
        sleep(0.5)