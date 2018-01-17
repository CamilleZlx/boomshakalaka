#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        length = len(digits)
        for i in range(length):
            num = num + 10**(length - i - 1)*digits[i]
        num = num +1
        length_ = len(str(num))
        nums = []
        for i in range(1, length_ + 1):
            t = num % 10
            nums.append(int(t))
            num = num // 10
        nums.reverse()
        return nums

