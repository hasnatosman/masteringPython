"""class Father:
    def farming(self):
        print('I can grow food.')


class Mother:
    def cooking(self):
        print('A can cook food.')

class Child(Father, Mother):
    def skills(self):
        print('I can play football.')


c = Child()
c.farming()
c.cooking()
c.skills()
"""


class Father:
    def skills(self):
        print('I am a programmer.')


class Mother:
    def skills(self):
        print('I can cook.')


class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)

        print('i love to play football.')


c = Child()
c.skills()