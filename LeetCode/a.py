#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_
#
# nums = [2, 6, 4, 8, 10, 9, 15]
# list1 = sorted(nums)
#
# is_same = [a == b for a, b in zip(nums, sorted(nums))]
#
# print(nums)
# print(list1)
#
# print(is_same.index(False))
# print(is_same[::-1].index(False))
# print(is_same)

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
n = len(cost)
min_cost0 = cost[0]
min_cost1 = cost[1]

for i in range(2,n):
    min_cost0 = min_cost1
    min_cost1 = min(min_cost0, min_cost1) + cost[i]
print(min(min_cost0, min_cost1))
