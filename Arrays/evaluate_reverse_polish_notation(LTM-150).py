class Solution:
    def evalRPN(self, s) -> int:
        st = []
        for i in s:
            if i.lstrip("-").isdigit():
                st.append(int(i))
            elif i in '+-/*':
                n1 = st.pop()
                n2 = st.pop()
                if i == '+':
                    st.append(n1+n2)
                    continue
                if i == '-':
                    st.append(n2-n1)
                    continue
                if i == '*':
                    st.append(n2*n1)
                    continue
                if i == '/':
                    st.append(int(n2/n1))
                    continue
        return st.pop()

    def evalRPN2(self, tokens) -> int:
        stack = []
        operators = {'+': lambda x, y: x + y,
                     '-': lambda x, y: x - y,
                     '*': lambda x, y: x * y,
                     '/': lambda x, y: int(x / y)}
        for val in tokens:
            if val in operators:
                # print (stack)
                y = int(stack.pop())
                x = int(stack.pop())

                result = operators[val](x, y)
                stack.append(result)
            else:
                stack.append(val)

        return stack.pop()

obj = Solution()
#print(obj.evalRPN(["4", "13", "5", "/", "+"]))
print(obj.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))