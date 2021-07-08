class Solution:
    def findRotation(self, mat, target) -> bool:
        for _ in range(4):
            if mat == target: return True
            mat = [list(x) for x in zip(*mat[::-1])]
        return False

obj = Solution()
obj.findRotation([[0,1],[1,0]], [[1,0],[0,1]])