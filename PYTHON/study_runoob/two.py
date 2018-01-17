#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

profit = [1000000, 600000, 400000, 200000, 100000, 0]
payment = [0.001, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
i = int(input("请输入利润："))
for index in range(0,6):
    if i > profit[index]:
        r += (i-profit[index])*payment[index]
        print(u"超过",profit[index],u"部分的提成是",(i-profit[index])*payment[index],u"元")
        i = profit[index]
print(r)
