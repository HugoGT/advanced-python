from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Pasaron ' + str(time_elapsed.total_seconds()) + ' segundos')
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 10000000):
        pass


@execution_time
def sum(a: int, b: int) -> int:
    return print(a + b)


@execution_time
def greeting(name = 'Hugo'):
    return print(f'Hola {name}')


@execution_time
def run():
    random_func()
    sum(5, 5)
    greeting()
    greeting('César')


if __name__ == '__main__':
    run()