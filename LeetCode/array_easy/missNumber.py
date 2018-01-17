#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        if nums[-1] == n-1:
            return n
        for i in range(n):
            if nums[i] == i:
                continue
            else:
                return i

    # return sum(range(len(nums)+1)) - sum(nums)

