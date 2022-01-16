class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        visited = set()
        stack = []
        while popped:
            elem = popped.pop(0)
            for item in pushed:
                if item not in visited:
                    visited.add(item)
                    stack.append(item)
                if item == elem and stack[-1] == elem:
                    stack.pop()
                    break
        if not stack:
            return True
        return False

    def validateStackSequences2(self, pushed, popped) -> bool:
        j = 0
        stack = []
        for item in pushed:
            stack.append(item)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j+=1
        return j == len(popped)

    # Time: O(n)
    # Space: O(n)


obj = Solution()
#print(obj.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
print(obj.validateStackSequences2([1,2,3,4,5], [4,5,3,2,1]))