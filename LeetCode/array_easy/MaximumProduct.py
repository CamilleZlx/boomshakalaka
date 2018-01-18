class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import itertools
        nums.sort()
        del nums[3:-3]
        return max(a*b*c for a, b, c in itertools.combinations(nums, 3))