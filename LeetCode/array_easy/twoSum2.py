#!~/anaconda/envs/python36/bin/python
#_*_ coding: utf-8 _*_

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) <= 1:
            return False
        buff_dict = {}
        for i in range(len(numbers)):
            if numbers[i] in buff_dict:
                index1 = min(buff_dict[numbers[i]]+1, i+1)
                index2 = max(buff_dict[numbers[i]]+1, i+1)
                return index1,index2
            else:
                buff_dict[target - numbers[i]] = i

