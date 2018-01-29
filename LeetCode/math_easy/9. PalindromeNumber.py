# 类似于第7题
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        temp, res = x, 0
        # while x:----------Time Limit Exceeded  ???
        while temp:  
            res = res * 10 + temp % 10
            temp = temp // 10
        return x == res
