# Class based on employee - separating to check decorators

class Player:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None


ply1 = Player("John", "Smith")
ply1.first = "Paul"

print(ply1.first)
print(ply1.email())
print(ply1.fullname)
del ply1.fullname
print(ply1.fullname)