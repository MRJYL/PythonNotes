def padding():
    print('\n')
# 新建类
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def sit(self):
        '''模拟蹲下命令'''
        print(self.name.title() + 'is now sitting')

    def roll_over(self):
        '''模拟小狗打滚明星'''
        print(self.name.title() + ' rolled over!')
my_dog = Dog('willie',6)
my_dog.roll_over()

your_dog = Dog('danhuang',3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

padding()

import Car

my_new_car = Car.Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odomeer()

my_new_car.odomter_reading = 3
my_new_car.read_odomeer()

my_new_car.update_odometer(10)
my_new_car.read_odomeer()

my_new_car.update_odometer(5)
my_new_car.read_odomeer()

my_new_car.update_odometer(23500)
print(my_new_car.odomter_reading)

my_new_car.increment_odometer(100)
print(my_new_car.odomter_reading)

padding()

my_tesla = Car.ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())

padding()

from collections import OrderedDict
# 有序字典
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
