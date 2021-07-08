class Solution:
    def replaceDigits(self, s: str) -> str:
        index_map = dict(zip(range(26), list('abcdefghijklmnopqrstuvwxyz')))
        char_map = dict(zip(list('abcdefghijklmnopqrstuvwxyz'), range(26)))
        res = ''
        for i in range(len(s)):
            if s[i].isalpha():
                res += s[i]
            if s[i].isdigit():
                digit = int(s[i])
                char = s[i-1]
                new_digit = char_map[char]+digit
                new_char = index_map[new_digit]
                res+=new_char
        return res

    def replaceDigits1(self, s: str) -> str:
        a = list(s)
        for i in range(1, len(a), 2):
            a[i] = chr(ord(a[i - 1]) + int(a[i]))
        return ''.join(a)

obj = Solution()
print(obj.replaceDigits1("a1c1e1"))
print(obj.replaceDigits1("a1b2c3d4e"))



