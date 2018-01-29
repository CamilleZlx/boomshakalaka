#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_left = 0
        sum_right = sum(nums)
        for index in range(len(nums)):
            sum_right -= nums[index]
            if sum_left == sum_right:
                return index
            sum_left += nums[index]
        return -1