#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1 or len(nums) > 50 or max(nums) < 0 or min(nums) > 99:
            return False
        nums_ = sorted(nums)
        if len(nums) == 1 & nums[0] == 0:
            return -1
        elif len(nums) == 1 & nums[0] != 0:
            return 0
        elif nums_[-1] >= 2*nums_[-2]:
            return nums.index(nums_[-1])
        else:
            return -1
