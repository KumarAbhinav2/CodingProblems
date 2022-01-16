
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # split the path by /
        for char in path.split('/'):
            # if . then no need to do anything and if found '' as well don't do anything
            if char == '.' or not char:
                continue
            # pop one elem out when found .., as we need to move one directory up
            elif char == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        # extra /  for having root added at the beginning
        return '/'+'/'.join(stack)

    # Time complexity: O(n)
    # space Complexity: O(2n), one for array and another one for string =~ O(n)