class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        x = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[x]:
                x += 1
                nums[x] = nums[i]
        return x + 1

