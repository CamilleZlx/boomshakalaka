#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(same) else len(nums) - same.index(False) - same[::-1].index(False)

