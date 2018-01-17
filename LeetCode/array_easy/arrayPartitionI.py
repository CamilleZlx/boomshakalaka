#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

class Solution:
    def arrayPairSum(self, nums):
        sum = 0
        n = len(nums)/2
        if n<1 or n>10000:
            return False
        if max(nums)>10000 or min(nums)<-10000:
            return False
        nums.sort()
        for i in range(len(nums)):
            if i % 2 == 0:
                sum += nums[i]
        return sum