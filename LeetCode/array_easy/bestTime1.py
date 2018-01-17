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
        max_profile = 0
        low_price = prices[0]
        for i in range(1, len(prices)):
            low_price = min(low_price, prices[i])
            max_profile = max(max_profile, prices[i]-low_price)
        return max_profile


