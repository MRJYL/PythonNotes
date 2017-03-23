pandding = '\n'

# 字典简介
alien = {'color':'green','points':5}
print(alien['color'])
print(alien['points'])
# 添加键值对
alien['position_x'] = 0
alien['position_y'] = 25
print(alien)
# 修改值
alien['color'] = 'yellow'
print(alien)
# 删除键值对
del alien['points']
print(alien)

favorite_language ={
    'jin:':'python',
    'wang':'python',
    'yang':'java',
    'lei':'javascript'
}
print(favorite_language)
print("lei's favorite language is " + favorite_language['lei'].title() + ".")
print(pandding)
# 遍历，乱序
for key in favorite_language.keys():
    print( 'key: ' + key )
print(pandding)
for value in favorite_language.values():
    print( 'value: ' + value )
print(pandding)

for key,value in favorite_language.items():
    print('\nkey: ' + key)
    print('value: ' + value)
print(pandding)
# 几个set去重
for value in set(favorite_language.values()):
    print('value: ' + value)

aliens = []
for alienNumb in range(30):
    newAlien = {'color':'green',"points":'5','speed':'slow'}
    aliens.append(newAlien)
print(len(aliens))

for alien in aliens[:5]:
    print(alien)


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if  len(languages) == 1:
        print( "\n" + name.title() + "'s favorite languages are:" + languages[-1].title() )
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print( "\t" + language.title())

# 嵌套
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        "first": 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for userName, userInfo in users.items():
    print('\nUserName: ' + userName)
    fullName = userInfo['first'] + userInfo['last']
    location = userInfo['location']

    print('\tFull name : ' + fullName.title())
    print('\nLocation: ' + location.title())

de