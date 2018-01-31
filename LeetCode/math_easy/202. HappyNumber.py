class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # for “loops endlessly” ----- define a list nums[],if num is not in nums,
        # nums.append(num), else ended
        nums = set()
        while n not in nums:
            nums.add(n)
            n = sum(pow(int(i),2) for i in str(n))
        return n == 1