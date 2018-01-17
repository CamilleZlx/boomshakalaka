#!/usr/bin/env python
# _*_ coding: utf-8 _*_

'''
假设有一个6*6的棋盘，每个格子里面有一个奖品（每个奖品的价值在100到1000之间），
现在要求从左上角开始到右下角结束，每次只能往右或往下走一个格子，
所经过的格子里的奖品归自己所有。问最多能收集价值多少的奖品。
DP算法适用于前一步的决策影响后一步决策的问题中。
本题蓝色方块的决策取决于其左边和上面的最优决策
对于蓝色部分a[i][j]只需要取max{a[i-1][j],a[i][j-1]}+a[i][j];
对于白色部分，只受左边或者上面的决策影响，
因此对于横向的a[i][j]应该取a[i][j-1]+a[i][j],
对于纵向的a[i][j]应该取a[i-1][j]+a[i][j]
'''

import random
count=0
a=[[0 for i in range(6)]for i in range(6)]

print("随机生成一个6*6的二维数组做为棋盘中的权值：")
for i in range(6):
    for j in range(6):
        a[i][j] = random.randint(100, 1000)
        print('%2d'%a[i][j],end=" ")
        count+=1
        if count%6==0:
            print("\n")
for i in range(1,6):
    a[0][i]=a[0][i-1]+a[0][i]
    a[i][0]=a[i-1][0]+a[i][0]
for i in range(1,6):
    for j in range(1,6):
        a[i][j]=max(a[i-1][j],a[i][j-1])+a[i][j]
print("变化后的数组：")
for i in range(6):
    for j in range(6):
        print('%2d'%a[i][j],end=" ")
        count+=1
        if count%6==0:
            print("\n")
print("最终得最大值为%d" %a[5][5])