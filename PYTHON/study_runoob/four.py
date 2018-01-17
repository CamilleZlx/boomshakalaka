#!~/anaconda/env/python36/bin/python
#_*_ coding: utf-8 _*_

year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日："))

months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

if 1 <= month <= 12:
    sums = months[month-1]
else:
    print("Error Date")

i = 0
if year % 400 == 0 or (year % 4 == 0 & year % 100 != 0):
    i = 1

daily = sums + day

if i == 1 & month > 2:
    daily = daily +1

print(u"这是今年的第",daily,u"天")

