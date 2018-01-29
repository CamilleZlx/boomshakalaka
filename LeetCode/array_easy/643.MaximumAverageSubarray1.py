class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # n = len(nums)-k+1
        # i, max_aver = 0, -float('inf')
        # while i < n:
        #     sum_, j = 0, 0
        #     while j < k:
        #         sum_ = sum_ + nums[i+j]
        #         j += 1
        #     max_aver = max(max_aver, sum_)
        #     i += 1
        # return(max_aver/k)

        sum_ , max_sum = 0, -float('inf')
        for i , num in enumerate(nums):
            sum_ += num
            if i >= k:
                sum_ -= nums[i-k] 
            if i >= k-1:
                max_sum = max(max_sum,sum_)
        return max_sum/float(k)
