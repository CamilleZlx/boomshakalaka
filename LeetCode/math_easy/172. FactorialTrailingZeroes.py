class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n >= 5:
            n = n // 5
            res = res + n
        return res


        # return 0 if n == 0 else n // 5 + self.trailingZeroes(n//5)