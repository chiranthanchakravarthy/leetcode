class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def canPartition(self, sqr, tgt, sum):
            if sqr==0:
                return tgt==sum
            
            return canPartition(self, sqr/10, tgt, sum + sqr%10) or canPartition(self, sqr/100, tgt, sum + sqr%100) or canPartition(self, sqr/1000, tgt, sum + sqr%1000) or canPartition(self, sqr/10000, tgt, sum + sqr%10000)

        sum=0
        for i in range(1,n+1):
            sqr=i*i
            if canPartition(self, sqr, i, 0):
                sum+=sqr

        return sum

        