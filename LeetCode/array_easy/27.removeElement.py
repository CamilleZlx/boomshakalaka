#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

class Solution:
    def removeElement(self, nums, val):
        if len(nums) < 0:
            return False
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)