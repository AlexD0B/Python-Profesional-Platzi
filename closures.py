# Hola 3 -> HolaHolaHola
# Facundo 2 -> FacundoFacundo
# Platzi 4 -> PlatziPlatziPlatziPlatzi

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes usar cadenas de texto"
        return string * n
    return repeater 

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola "))
    repeat_8 = make_repeater_of(8)
    print(repeat_8("Go"))

if __name__ == '__main__':
    run()