class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 时间超出限制
        # n = len(nums)
        # major = 0
        # if n == 0:
        #     return 0 
        # for i in range(len(nums)):
        #     if nums.count(nums[i]) > n // 2:
        #         return nums[i]

        # 题目描述这个数一定存在，所以nums的中间数一定是answer
        return sorted(nums)[len(nums)/2]

        # 时间超出限制
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j]:
        #             count += 1
        #         if count > len(nums)//2:
        #             return nums[i]
