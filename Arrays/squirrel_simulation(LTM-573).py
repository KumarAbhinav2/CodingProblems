class Solution:
    def dist(self, p1, p2):
        return abs(p1[0] - p2[0])+abs(p1[1] - p2[1])

    def minDistance(self, height, width, tree, squirrel, nuts):
        nuts_tree_distance = sum(2*self.dist(tree, nut) for nut in nuts)
        return min(nuts_tree_distance+(self.dist(nut, squirrel) - self.dist(nut, tree)) for nut in nuts)

obj  = Solution()
print(obj.minDistance(5, 7, [2, 2], [4,4], [[3,0], [2,5]]))