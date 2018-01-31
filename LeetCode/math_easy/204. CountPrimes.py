class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2,int(pow(n,0.5))+1):
            if primes[i]:
                primes[i*i:n:i] = [False] * len(primes[i*i:n:i])
        return sum(primes)

        # for 
        #   ...
        #   break  
        # else
        #   ...
        # 当for循环结束并为空时，执行else语句，如果没有break，不管for执行的结果如何 都会执行else
        # Time Limit Exceeded
        # nums = []
        # for i in range(2,n):
        #     j = 2
        #     for j in range(2,i):
        #         if i % j == 0:
        #             break
        #     else:
        #         nums.append(i)
        # return len(nums)
                    
