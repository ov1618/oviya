#polymorphism
'''
class Dog():
    def sound(self):
        print('bark')
class Cat():
    def sound(self):
        print('meow')
def mammal(animal):
    animal.sound()

dog=dog()
cat=cat()
mammal(dog)
'''
#using super class
class BaseClass():
    print('hi')
    def __init__(self,water):
        print('base')
        self.test_water=water
    def get_water(self,bottle):
        print('getting hot {0} in {1}'.format(self.test_water,bottle))
class TestFn(BaseClass):
    def get_water(self,bottle='office bottle'):
        self.bottle=bottle
        super(TestFn,self).get_water(self.bottle)
        print('getting cold {0} from my class in {1}'.format(self.test_water,bottle))
    def display_name(self):
        print(self.test_water)
o=TestFn('water')
o.get_water()
