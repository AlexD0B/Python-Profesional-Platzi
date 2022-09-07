def mayus(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura    

@mayus
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

print(mensaje("alex"))