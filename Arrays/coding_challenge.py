"""
input = [2, 4, 7, 3, 2, 4, 6]
output = [2, 4, 3], [7, 2], [4, 6]
"""

class Solution1:
    def sumlist(self, lst):
        res = []
        curr_sum = sum(lst)
        div_val = curr_sum//3

        while len(res) != 3:
            stack = []
            while lst:
                if i < div_val and sum(stack)+i <= div_val:
                    stack.append(lst.pop(0))
                else:
                    continue
            res.append(stack)
        return res


class Solution:

    def sumlist(self, lst):
        lst.sort()  # O(nlogn)
        res1, res2, res3 = [], [], []
        while lst:   # O(n)
            elem = lst.pop()
            min_lst = min([res1, res2, res3], key=sum)
            min_lst.append(elem)
        return (res1, res2, res3) if all((res1, res2, res3)) else -1

obj = Solution()
print(obj.sumlist([2, 4, 7, 3, 2, 4, 6]))
print(obj.sumlist([3, 4, 6, 4, 7, 4, 2]))
print(obj.sumlist([8, 5, 5, 2, 4, 5, 3]))
print(obj.sumlist([1,1]))


