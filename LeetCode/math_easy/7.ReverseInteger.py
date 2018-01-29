class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = 1
        if x < 0:
            temp = -1
        x = abs(x)
        x_ = 0
        while x != 0:
            x_ = x_ * 10 + x % 10
            x = x // 10
            if x_ > 2**31:
                return 0
        return x_*temp