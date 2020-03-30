#File person.py (final)
from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay*(1 + percent))
    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)
        #return '[Person: {self.name}, {self.pay}]'.format(self=self) #Same as previous

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent+bonus)
    '''
    # if we don't use "from classtools import AttrDisplay"
    # we have to type in this way:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent+bonus)
    def __getattr__(self, attr):
        return getattr(self.person, attr)
    def __str__(self):
        return str(self.person)
    '''

if __name__ == '__main__':
    #self-test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(),sue.lastName())
    sue.giveRaise(.10)
    print(bob)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    print(tom.lastName())
    print(tom)
    tom.giveRaise(.10,.50)
    print(tom)
    print("------------------------------------------")
    
class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaise(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)

if __name__ == '__main__':
    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaise(.10)
    development.showAll()
    print("------------------------------------------")