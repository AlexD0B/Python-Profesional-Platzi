from datetime import datetime

def execution_time(func):
    def wrappler(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrappler

@execution_time
def random_func():
    for _ in range (1,100000):
        pass
@execution_time
def saludo(nombre="Alex"):
    print("Hola " + nombre)

random_func()
saludo("Pepe")
