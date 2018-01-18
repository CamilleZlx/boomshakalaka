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
import itertools
nums = [1,2 ,3, 4, 5,6,7,8,9,6,7] 
nums.sort()
del nums[3:-3]
print(nums)
print(max(a*b*c for a, b, c in itertools.combinations(nums, 3)))