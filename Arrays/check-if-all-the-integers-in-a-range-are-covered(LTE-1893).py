
class Solution:
    def isCovered(self, ranges, left: int, right: int):
        ranges.sort()
        target_range = list(range(left, right+1))
        for r in ranges:
            while target_range:
                elem = target_range[0]
                if elem in range(r[0], r[1]+1):
                    target_range.pop(0)
                    continue
                else:
                    break
        if target_range: return False
        return True

    def isCovered2(self, ranges, left, right):
        return all(any(l<=i<=r for l,r in ranges) for i in range(left, right+1))




obj = Solution()
print(obj.isCovered([[1,2],[3,4],[5,6]], 2, 5))
print(obj.isCovered([[1,10],[10,20]], 21, 21))
print(obj.isCovered([[1,1]], 1, 50))
print(obj.isCovered([[1,1]], 1, 1))
print(obj.isCovered([[1, 50]], 1, 50))