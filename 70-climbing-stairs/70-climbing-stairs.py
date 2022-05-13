class Solution(object):
    def climbStairs(self, n):
        first, second = 1, 1
        
        for i in range(n - 1):
            first, second = second, first + second
        return second