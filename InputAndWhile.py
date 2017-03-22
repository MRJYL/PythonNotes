# 输入
name = input("Please enter your name: \n")
print('Hello, ' + name + "!")

# 判断年龄
doWhile = True
age = input('How old are you?\n')
while doWhile:
    if age == 'quit':
        break
    else:
        age = int(age)
        if age > 18:
            print('You are a man')
        else:
            print('You are a boy')
        age = input( 'How old are you?\n' )


# 删除
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets: pets.remove('cat')
print(pets)
# 验证用户
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    # 显示所有已  的用户
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
       print(confirmed_user.title())

# 调查问卷
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
