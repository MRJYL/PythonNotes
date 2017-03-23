
file_name = 'pi_digits.txt'
def padding():
    print('\n')
#打开文件 with关键字：在不需要访问文件后将其自动关闭
with open(file_name) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# # 手动关闭文件
# file_object= open('pi_digits.txt')
# contents = file_object.read()
# print(contents)
# file_object.close()

padding()

# 逐行读取
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

padding()
# 常见一个包含文件各行内容的list
with open(file_name) as file_object:
    lines = file_object.readlines()
print(lines)
for line in lines:
    print(line.rstrip())
padding()

# 使用文件的内容
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

# 写入文件
file_name = 'programming.txt'
with open(file_name,'w') as file_object:
    file_object.write('I love programming\n')
    file_object.write('I love creating new games.\n')

# 异常处理
try :
    print(5/0)
except ZeroDivisionError:
    print('error')

# 错误处理机制 try-except-else
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('divide by 0!')
    else:
        print(answer)


def count_words(filename:str):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print( msg )
    else:
        words = contents.split()
        num_words = len(words)
        print( "The file " + filename + " has about " + str( num_words ) + " words." )

count_words('programming.txt')

import json

def get_stored_name(file_name = 'username.json'):
    try:
        with open(file_name) as f_obj:
            user_name = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return user_name

def store_name(file_name = 'username.json'):
    user_name = input('enter your username: ')
    with open(file_name,'w') as f_obj:
        json.dump(user_name,f_obj)
        print('we will remenber your name !')

def get_user(file_name = 'username.json'):
    user_name = get_stored_name(file_name)
    if  user_name:
        print('welcome back ' + user_name + '!' )
    else:
        store_name(file_name)
get_user()