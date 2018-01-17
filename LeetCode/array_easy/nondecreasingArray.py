#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 1 or len(nums) > 10000:
            return False
        one = nums[:]
        two = nums[:]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                one[i] = nums[i+1]
                two[i+1] = nums[i]
                break
        return one == sorted(one) or two == sorted(two)
