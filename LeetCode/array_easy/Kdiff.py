#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

import collections

class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # if len(nums) <= 1 or len(nums) > 10000:
        #     return 0
        # nums_ = sorted(nums)
        # paris = []
        # for i in range(len(nums_)):
        #     if nums_[i] + k in nums_:
        #         if [nums_[i], nums_[i] + k] not in paris:
        #             if k == 0:
        #                 if nums_.count(nums_[i]) >= 2:
        #                     paris.append([nums_[i], nums_[i] + k])
        #             elif k > 0:
        #                 paris.append([nums_[i], nums_[i] + k])
        #             else:
        #                 break
        # return len(paris)

        if k > 0:

            return len(set(nums) & set(n + k for n in nums))
        elif k == 0:
            sum(v > 1 for v in collections.Counter(nums).values())
        else:
            return 0



