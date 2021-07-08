class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [c == '0' for c in s]
        pre = 0
        for i in range(1, len(s)):
            if i >= minJump:
                pre += dp[i - minJump]
            if i > maxJump:
                pre -= dp[i-maxJump - 1]
            dp[i] &= pre > 0
        return dp[-1]

    def canReach_bf(self, s: str, minJump: int, maxJump: int) -> bool:
        import collections
        q, max_reached = collections.deque([0]), 0
        while q:
            curr_i = q.popleft()
            if curr_i == len(s)-1:
                return True
            start = max(curr_i+minJump, max_reached)
            for i in range(start, min(curr_i+maxJump+1, len(s)-1)):
                if s[i] == '0':
                    q.append(i)
            max_reached  = curr_i+maxJump
        return False

obj = Solution()
print(obj.canReach("011010", 2, 3))
print(obj.canReach("01101110", 2, 3))
print(obj.canReach("0100001000", 2, 4))


