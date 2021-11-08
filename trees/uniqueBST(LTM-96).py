class Solution:
    '''
    We can start with below approach
    1) iterate till given number, and for each number say(i) we first generate all BSTs from 1 to i-1
    2) then generate all BSTs from i+1 to n
    3) generate all combinations of left and right branch with i on the root
    '''
    def numTrees(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        res = 0
        for i in range(n):
            l_tree = self.numTrees(i)
            r_tree = self.numTrees(n-i-1)
            res += (l_tree * r_tree)
        return res

    def rec(self, n, cache):
        if n == 0:
            return 1
        if n == 1:
            return 1
        if cache.get(n , -1) != -1:
            return cache[n]
        res = 0
        for i in range(n):
            l_tree = self.rec(i, cache)
            r_tree = self.rec(n-i-1, cache)
            res += (l_tree * r_tree)
        return res

    def numTrees_dp(self, n):
        cache = {}
        return self.rec(n, cache)

obj = Solution()
print(obj.numTrees(3))
print(obj.numTrees_dp(3))