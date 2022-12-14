from time import sleep

def fibonacci_gen():
    a, b = 0, 1
    max_num = 1600
    contador = a
    while max_num > contador:
        yield a
        a, b = b, a+b
        contador = a


if __name__ == "__main__":
    fibonacci = fibonacci_gen()
    for element in fibonacci:
        print(element)
        sleep(0.1)