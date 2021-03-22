class Road:
    __length = 5000
    __width = 20

    def __init__(self):
        a_mass = Road.__length * Road.__width * 25 * 5/1000
        print(a_mass, 'т')


r = Road()
