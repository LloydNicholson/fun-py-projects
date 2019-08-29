import math


class Dog:
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ALL INSTANCES OF THE CLASS
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    # methods
    def bark(self):
        print(f'{self.name} barked!! Woof woof!')


rust = Dog(breed='Labrador', name='Rusty')
print(rust.breed)
print(rust.name)
print(rust.species)
rust.bark()


class Circle:
    pi = math.pi

    def __init__(self, radius=1):
        self.radius = radius
        # a convention used to define a class attribute
        self.area = radius * radius * Circle.pi

    def get_circumference(self):
        return Circle.pi * self.radius * 2

    # using magic method when function str() is called on Circle instance
    def __str__(self):
        return f'Circle radius is {self.radius} and pi is {Circle.pi}, which equals {self.get_circumference()}'


my_circle = Circle(radius=5)
print(my_circle.get_circumference())
print(str(my_circle))

# class Animal:
#     def __init__(self):
#         print('ANIMAL CREATED')
#
#     def who_am_i(self):
#         print('I am an animal')
#
#     def eat(self):
#         print('I am eating')
#
#
# my_animal = Animal()
# print(my_animal)

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')


class Dog(Animal):
    def speak(self):
        print(f'{self.name} said woof')


class Cat(Animal):
    def speak(self):
        print(f'{self.name} said meow')


fido = Dog('Fido')
isis = Cat('Isis')
fido.speak()
isis.speak()

# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print('Dog created')
#
#     def who_am_i(self):
#         print('I am a dog')
#
#     def bark(self):
#         print('I barked')
#
#
# my_dog = Dog()
# my_animal.who_am_i()
# my_dog.who_am_i()
