import math


class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0
        self.listOfSpeeds = []

    def say_state(self):
        print("I'm going {} kph!".format(self.speed))

    def add_to_speed_list(self):
        self.listOfSpeeds.append(self.speed)

    def accelerate(self):
        self.speed += 5
        self.add_to_speed_list()

    def brake(self):
        if len(self.listOfSpeeds) > 0:
            self.speed -= 5
            if self.speed < 0:
                self.speed = 0

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def change_speed_to(self, new_speed):
        if new_speed < 0:
            self.speed = 0
        self.speed = new_speed
        self.add_to_speed_list()

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass

    def top_speed(self):
        if len(self.listOfSpeeds) > 0:
            self.listOfSpeeds.sort()
            if len(self.listOfSpeeds) > 2:
                del self.listOfSpeeds[0:-2]
            print(self.listOfSpeeds)
            return self.listOfSpeeds[-1]


if __name__ == '__main__':

    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                       "show [O]dometer, [T]op speed, [I]ncrease speed to or show average [S]peed?").upper()
        if action not in "ABOSTI" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        elif action == 'T':
            print('The car\'s top speed was {}'.format(my_car.top_speed()))
        elif action == 'I':
            received_speed = input('New speed is: ')
            my_car.change_speed_to(int(received_speed))
        my_car.step()
        my_car.say_state()
