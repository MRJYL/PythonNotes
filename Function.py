# 定义函数
def padding():
    print('\n')

def greet_user(userName):
    """fasjflasjfkl"""
    print('Hello ' + userName +'!')

# message = input('name :')
message = 'jinyulong'
greet_user(message)

def describe_pet(animal_type, pet_name):
    """显示 物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# 位置参数
describe_pet('hamster', 'harry')
# 关键字参数
describe_pet(pet_name='harry',animal_type='hamster')
# 设置默认值，依然会视为位置参数，需要把未设置默认值的形参放在前边
def pet(pet_name,animal_type='dog'):
    """显示 物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# 位置参数
pet('harry')
# 关键字参数
pet(pet_name='harry',animal_type='hamster')

# 返回值
def getFormattedName(firstName:str,lastName:str):
    fullName ='\n' + firstName + lastName
    return fullName.title();
print(getFormattedName('jin','yulong'))
padding()

# 让实参编程可选,非空字符串为True
def getOptionalName(firstName:str,lastName:str,middleName = ""):
    if  middleName:
        fullName = firstName + middleName + lastName
    else:
        fullName = firstName + lastName
    return fullName.title()
print(getOptionalName('jin','yu'))
print(getOptionalName('jin','yu','long'))
print(getOptionalName(firstName = 'jin',middleName = 'yu',lastName = 'long'))
padding()

# 返回字典
def returnDic(firstName,lastName,age = ''):
    person = {'firstName':firstName,'lastName':lastName}
    if age:
        person['age'] = age
    return person
print(returnDic('jin','yulong'))
print(returnDic('jin','yulong','13'))
padding()

# 传递列表
def transList(firstList:list):
    firstList[-1] = 'wife'

names = ['jin','yao']

# 禁止函数修改列表
transList(names[:])
print(names)
# 允许修改
transList(names)
print(names)
padding()


# 传递任意数量的实参 *toppings为空元组 必须将接纳任意数量的形参放在最后
def make_pizza(size = '8',*toppings):
    print(toppings)
    for topping in toppings:
        print('- ' + str(size) + '-inch '+ topping)

make_pizza( 'pepperoni')
padding()
make_pizza(16,'mushrooms','green peppers','extra cheese')
padding()

# 使用任意数量的关键字实参

def build_profile(first, last, **user_info):
    """创建一个字典 其中包含    的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
      profile[key] = value
    return profile
user_profile = build_profile( 'albert', 'einstein', location='princeton',
                              field='physics' )
print( user_profile )
# # 函数模块儿化
# import HelloWorld
# HelloWorld.helloWorld()
# # 指定函数导入
# from List import pointMessage
# pointMessage()
# # 别名导入
# from List import  importMessag as IM
# IM()
# # 导入所有函数(不建议这么做），尽量使用制定函数导入和点语法访问函数
# from HelloWorld import  *
# helloWorld()
