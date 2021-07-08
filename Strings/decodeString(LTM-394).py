class Solution:
    def decodeString(self, s: str) -> str:
        _stack = []
        num = 0
        string = ''
        for c in s:
            if c in '0123456789':
                num = num*10+int(c)
            elif c == '[':
                _stack.append(string)
                _stack.append(num)
                num=0
                string=''
            elif c.isalpha():
                string+=c
            elif c == ']':
                n = _stack.pop()
                p_str = _stack.pop()
                string = p_str+ string*n
        return string

    def decodeString2(self, s):
        num = ''
        _stack = []
        _stack.append(['', 1])
        for c in s:
            if c in '0123456789':
                num += c
            elif c == '[':
                _stack.append(['', int(num)])
                num = ''
            elif c.isalpha():
                _stack[-1][0] += c
            else:
                st, n = _stack.pop()
                _stack[-1][0] += st*n
        return _stack[0][0]


obj = Solution()
obj.decodeString("3[a]2[bc]")