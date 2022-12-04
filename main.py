class Animal:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.kindness = 0

    def live(self):
        print(self.name, 'is alive')


    def sleep(self):
        print(self.name, 'is sleeping')
    def statistics(self):     
        print('Name:',self.name,'Kindness:',self.kindness, 'Age:',self.age)

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def mewing(self):
        print(self.name,'is mewing')
        self.kindness+=2



class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def barking(self):
        print(self.name,'is barking')
        self.kindness +=2


class Humster(Animal):
    def __init__(self, name):
        super().__init__(name)

    def run(self):
        print(self.name, 'running in a wheel')
        self.kindness += 2
obj = Cat('Cat1')
obj.live()
obj2 = Dog('Dog1')
obj2.live()
obj3 = Humster('Humster1')
obj3.live()
obj3.sleep()
obj2.sleep()
obj.sleep()
obj.mewing()
obj2.barking()
obj3.run()
obj3.statistics()
obj2.statistics()
obj.statistics()




