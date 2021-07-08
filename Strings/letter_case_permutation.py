class Solution:
    def letterCasePermutation(self, S: str):
        visited = set()
        if not S.isalnum() or S.isdigit():
            return [S]

        def rec(s, i):
            if s not in visited:
                visited.add(s)
            if i > len(S) - 1:
                return
            c = s[i]
            if c.isalpha():
                s = list(s)
                s[i] = c.lower()
                s = ''.join(s)
                rec(s, i + 1)
                s = list(s)
                s[i] = c.upper()
                s = ''.join(s)
                rec(s, i + 1)

        rec(S, i=0)
        return list(visited)

obj = Solution()
print(obj.letterCasePermutation('a12b'))
print(obj.letterCasePermutation("a1b2"))
print(obj.letterCasePermutation("3z4"))
print(obj.letterCasePermutation("12345"))
print(obj.letterCasePermutation("0"))