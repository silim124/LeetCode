class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        def dfs(l, r, comb):
            if l == n and r == n:
                print(comb)
                res.append(comb)
                return
            if l < n:
                dfs(l + 1, r, comb + "(")
            if r < l:
                dfs(l, r + 1, comb + ")")
        
        dfs(0, 0, "")
        return res