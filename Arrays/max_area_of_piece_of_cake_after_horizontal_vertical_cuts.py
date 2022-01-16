class Solution:
    def maxArea(self, h: int, w: int, hc, vc) -> int:
        hc.sort()
        vc.sort()
        max_hc = max(hc[0], h - hc[-1])
        max_vc = max(vc[0], w - vc[-1])
        for i in range(1, len(hc)):
            diff = hc[i] - hc[i - 1]
            max_hc = max(max_hc, diff)
        for i in range(1, len(vc)):
            diff = vc[i] - vc[i - 1]
            max_vc = max(max_vc, diff)
        return (max_hc * max_vc) % (10**9 + 7)

obj = Solution()
print(obj.maxArea(5, 2, [3, 1, 2], [1]))
