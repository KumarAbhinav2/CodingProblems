class Solution:
    def splitString(self, s: str) -> bool:
        def solve(s, i, length, prev, splits):
            if i == len(s) and splits >= 2:
                return True
            while i + length <= len(s):
                cur = int(s[i:i + length])  # convert s[i:i + length] to integer
                length += 1
                # if above converted integer is not equal to prev - 1, try increasing the length
                if prev != -1 and cur != prev - 1: continue
                # if it is equal to prev - 1, recurse and make splits for remaining index
                if solve(s, i + length - 1, 1, cur, splits + 1):
                    return True
            return False

        return solve(s, 0, 1, -1, 0)


obj = Solution()
obj.splitString('050043')



