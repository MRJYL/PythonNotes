pandding = '\n'

# 简单示例
print('简单实例')
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if  car.lower() == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print(pandding)
# 与或非运算
print('与或非运算')
age_0 = 26
age_1 = 29
print(age_0 <= 20 or age_0 <= age_1)
print(age_0 <=age_1 and age_0 > 27)
# 判断是否包含
fruts = ['apple','banana','oriange']
print('apple' in fruts)
print('peach' in fruts)

if  'peach' not in fruts:
    print('peach'.title() + ' not in fruits')
print(pandding)
# 布尔表达式
tureCond = True
falseCond = False

# if语句
age = 12
if age<4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")




