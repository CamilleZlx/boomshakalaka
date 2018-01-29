class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        res = 0
        p = 'I'
        for i in s[::-1]:
            if d[i] < d[p]:
                res = res - d[i]
            else:
                res += d[i]
            p = i
        return res