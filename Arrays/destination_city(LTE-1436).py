class Solution:
    def destCity(self, paths) -> str:
        dest = set(path[1] for path in paths)
        source = set(path[0] for path in paths)
        return dest.difference(source).pop()

    # Time: O(n)
    # Space: O(n)

obj = Solution()
print(obj.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))