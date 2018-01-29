#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n < 2 or n > 1000:
            return 0
        min_cost0 = cost[0]
        min_cost1 = cost[1]
        for i in range(2,n):
            min_cost0 = min_cost1
            min_cost1 = min(min_cost0, min_cost1) + cost[i]
        return min(min_cost0, min_cost1)

 #    10 15 20
 #    [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]