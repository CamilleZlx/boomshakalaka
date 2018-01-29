#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        n = len(bits)
        if n < 1 or n > 1000:
            return False
        index = 0
        while index < n:
            if index == n-1:
                return True
            if bits[index] == 1:
                index += 2
            else:
                index += 1
        return False
