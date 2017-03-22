class Car():
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odomter_reading = 0
    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odomeer(self):
        """打印一条指出 程的消息 """
        print("This car has " + str(self.odomter_reading) + " miles on it.")

    def update_odometer(self, mileage):
         """将 程表读数设置为指定的值"""
         if mileage >= self.odomter_reading:
             self.odomter_reading = mileage
         else:
             print( "You can't roll back an odometer!" )

    def increment_odometer(self, miles):
        """将 程表读数增加指定的量"""
        self.odomter_reading += miles

class Battery():
    '''一次模拟 电动汽车电瓶的简单尝试'''
    def __init__(self,battery_size=60):
        self.battery_size = battery_size

    def describe_battery(self):
        print( "This car has a " + str( self.battery_size ) + "-kWh battery." )

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str( range )
        message += " miles on a full charge."
        print( message )

class ElectricCar(Car):
    '''模拟电动汽车的独特之处'''
    def __init__(self,make,model,year):
        '''初始化父类的属性，再初始化电动汽车特有的属性'''
        super().__init__(make,model,year)
        self.battery = Battery()
