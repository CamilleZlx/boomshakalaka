class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        conut = 0
        max_count = 0
        n = len(nums)
        while i < n:
            if nums[i] == 1:
                conut += 1
                i +=1
                max_count = max(max_count, conut)
            else:
                conut = 0
                i += 1
        return max_count


                    

    # [1,1,0,1,1,1]
                

        