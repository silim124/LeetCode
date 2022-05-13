class Solution(object):
    def climbStairs(self, n):
        first, second = 1, 1
        
        for i in range(n - 1):
            tmp = first
            first = first + second
            second = tmp
        return first