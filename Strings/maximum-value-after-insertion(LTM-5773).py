class Solution:
    def maxValue(self, n: str, x: int) -> str:
        sign = True if n[0] == '-' else False

        def minVal(n, x):
            nums = list(n)
            pos = len(n)
            for i, c in enumerate(nums):
                if int(c) <= x:
                    continue
                else:
                    pos = i
                    break
            nums.insert(pos, str(x))
            return '-'+''.join(nums)

        def maxVal(n, x):
            nums = list(n)
            pos = len(n)
            for i, c in enumerate(nums):
                if int(c) >= x:
                    continue
                else:
                    pos = i
                    break
            nums.insert(pos, str(x))
            return ''.join(nums)

        if sign:
            return minVal(n[1:], x)
        return maxVal(n, x)

obj = Solution()
print(obj.maxValue("28824579515", 8))
print(obj.maxValue("-132", 3))