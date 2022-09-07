from xmlrpc.client import Boolean


def primality(integer: int) -> Boolean:
    if integer % 2 == 0:
        return True
    else:
        return False

def run():
    print(primality(11))

if __name__ == '__main__':
    run()