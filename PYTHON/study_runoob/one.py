#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

num = 0
list = [1,2,3,4]

for i in list:
    for j in list:
        if(i == j):
            continue
        for k in list:
            if(i == k) or (j == k):
                continue
            num += 1
            print(i,j,k)
print("总数为:",num)

