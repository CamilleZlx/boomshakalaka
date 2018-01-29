#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        for i in range(len(prices)-1):
            total = 0
            if ( prices[i+1] > prices[i]):
                total += prices[i+1] - prices[i]
        return total
