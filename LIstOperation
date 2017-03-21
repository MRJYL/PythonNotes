# coding:utf-8
padding = "\n"

elements = ['harry','amanda','angle','zoo','jungle']
print(elements)
print(padding)

# for循环,缩进来控制循环体
print("for循环")
for title in elements :
    print("title is " + title.title() + '.')
    print("second line")
print("结束for循环")
print(padding)
# print(padding)

# range（a,b）创建一个 a<= x <b 的list
print("range（a,b）创建一个 a<= x <b 的list")
print(range(1,11))
print(list(range(1,11)))
print(padding)

# range(a,b,n) 创建一个 a<= x <b ，跨度为n的list
print("range(a,b,n) 创建一个 a<= x <b ，跨度为n的list")
print(range(2,11,2))
print(list(range(2,11,2)))
print(padding)

# 取10以内的乘方
print("取10以内的乘方")
squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)
print(padding)

# 对list简单的数据统计
print("对list简单的数据统计")
digits = list(range(1,101))
print(min(digits))
print(max(digits))
print(sum(digits))
print(padding)

# 列表解析
print("列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素")
squares = [value ** 3 for value in range(1,11)]
print(squares)
print(padding)

# 切片
print("切片")
players = ['harry','ron','hermine','marfu','panci']
print(players[0:3])
print(players[3:5])
# 不制定其实索引，从开始
print(players[:3])
# 不指定终止索引，自动到最后
print(players[2:])
print(players[-2:])

print([player for player in players[:3]])
print(padding)
# 复制列表,不能直接用 copy_players = players（浅拷贝）
copy_players = players[:] # 深拷贝
print(players)
print(copy_players)
players.append('chiu')
copy_players.append('dian')
print(players)
print(copy_players)
print(padding)

# 元组 和数组类型类似，但不用[],而用()，可以理解为不可变数组
print('元组')
dimensions = (200,50)
print(dimensions[0])
# dimensions[0] = 100 error，不可变
dimensions = (400,100)
print(dimensions)
