# _*_ coding:utf-8 _*_
#python2.7

import csv

aFile = open('C:/Users/Camille/Desktop/a.csv', 'r')

aInfo = csv.reader(aFile)
a=[]
a=list()
for info in aInfo:
    a.append(info)
print a
# for index in range(len(b)):
#     a[index+1].extend(b[index])
#     abcsv.writerow(a[index+1])

