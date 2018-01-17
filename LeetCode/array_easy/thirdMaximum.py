#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort()
        if len(nums) <= 2:
            return nums[-1]
        else:
            return nums[-3]

        # return sorted(set(nums))[-3] if len(set(nums)) > 2 else max(nums)

