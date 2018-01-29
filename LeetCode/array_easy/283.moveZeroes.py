#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)

# nums = [0, 1, 0, 3, 12]
# zero = 0  # records the position of "0"
# for i in range(len(nums)):
#     if nums[i] != 0:
#         nums[i], nums[zero] = nums[zero], nums[i]
#         zero += 1
# print(nums)
