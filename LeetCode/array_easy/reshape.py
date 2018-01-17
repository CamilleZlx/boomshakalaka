#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row = len(nums)
        col = len(nums[0])
        x = row * col
        nums_ = []
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                nums_.append(nums[i][j])
        if r * c == x:
            nums_new = []
            for i in range(r):
                nums_new = nums_new +[nums_[c*i:c*(i+1)]]
            return nums_new
        else:
            return nums