#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

import collections

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 50000 or len(nums) < 1 or max(nums) > 49999 or min(nums) < 0:
            return False
        nums_map = collections.defaultdict(list)
        degree = 0
        min_length = float('inf')
        for index, num in enumerate(nums):
            nums_map[num].append(index)
            degree = max(degree, len(nums_map[num]))
        for num, indices in nums_map.items():
            if len(indices) == degree:
                min_length = min(min_length, indices[-1] - indices[0] + 1)
        return min_length


