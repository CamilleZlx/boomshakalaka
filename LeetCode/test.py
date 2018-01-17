#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_
#leetcode前 Python学习测试

# 1.python标准数据类型
#   数字 Numbers  (int long float complex)
#   字符串 String " "
#   列表 List [] [value,value,......]
#   元组 Tuple () 类似于list 不能赋值 相当于只读列表 (value,value,......)
#   字典 Dictionary {key:value,key:value,......}
num = 1
print(num)
str1 = "hello world!"
print(str1)
list1 = ['a','b','c']
print(list1)
tup = ('aa','bb','cc')
print(tup)
dict1 = {}
dict1['one'] = 'this is one'
dict1[2] = 'this is two'
dict2 = {'1':'aa','2':'bb','3':'cc'}
print(dict1['one'])
print(dict1[2])
print(dict2)
print(dict2.keys())
print(dict2.values())
print("=================================")

# 2.运算符
#   算术运算符 : 加+ 减- 乘* 除/ 取模% 幂** 取整//
#   比较(关系)运算符 : 等于== 不等于!= 不等于<> 大于> 小于< 大于等于>= 小于等于<=
#   赋值运算符 : 简单的赋值= 加法赋值+= 减法赋值-= 乘法赋值*= 除法赋值/= 取模赋值%= 幂赋值**= 取整赋值//=
#   逻辑运算符 :  与and, x and y ,如果x为false，x and y 返回false，否则返回y的计算值
#               或or, x or y ,如果x非0，返回x的值，否则返回y的计算值
#               非not, not x ,如果 x 为 True，返回 False 。如果 x 为 False，它返回 True
#   位运算符 : 与& 或| 异或^ 取反~ 左移动<< 右移动>>
#   成员运算符 :  in : 如果在指定的序列中找到值返回 True，否则返回 False。
#               not in : 如果在指定的序列中没有找到值返回 True，否则返回 False。
#   身份运算符 :  is : 判断两个标识符是不是引用自一个对象
#               not is : 断两个标识符是不是引用自不同对象
#   运算符优先级

# 位运算符
a = 60  # 0110 1100
b = 13  # 0000 1101
c = 0
c = a & b
print(c)
c = a | b
print(c)
c = a ^ b
print(c)
c = ~a
print(c)
c = a << 2
print(c)
c = a >> 2
print(c)
print("=================================")

# 3.条件语句
# if 判断条件1:
#    执行语句……
# elif 判断条件2:
#    执行语句……
# elif 判断条件3:
#    执行语句……
# elif 判断条件4:
#    执行语句……
# else:
#    执行语句……

# 4.循环语句
#   while循环
#   for循环
#   嵌套循环
#   循环控制语句 : break语句(终止循环) continue语句(跳出本次循环) pass语句(空语句，不做任何事情，一般用做占位语句)

import time
ticks = time.time()
print(ticks)

# 如果要给函数内的全局变量赋值，必须使用 global 语句
Money = 2000
def AddMoney():
    global Money
    Money = Money + 1
print(Money)
AddMoney()
print(Money)

# python3.x中raw_input( )和input( )进行了整合，去除了raw_input( )，仅保留了input( )函数，
# 其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。
str = input("请输入：")
print("你输入的内容是: ", str)









