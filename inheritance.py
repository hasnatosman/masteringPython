class Vehicle:
    def general_usage(self):
        print('General usage: Transportation.')


class Car(Vehicle):
    def __init__(self):
        print('I am a car.')
        self.wheels = 4
        self.roof = True

    def usage(self):
        self.general_usage()
        print('Usages: Work and family.')


class Motor(Vehicle):
    def __init__(self):
        print('I am a Motor.')
        self.wheels = 2
        self.roof = False

    def usage(self):
        self.general_usage()
        print('Usages: Work and vacations.')


"""
c = Car()
#c.general_usage()
c.usage()
m = Motor()
#m.general_usage()
m.usage()
"""

c = Car()
print(isinstance(c, Motor))
m = Motor()
print(isinstance(m, Car))
