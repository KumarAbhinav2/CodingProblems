class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {
            '6':'9',
            '8':'8',
            '9':'6',
            '0':'0'
        }
        if len(num) == 1:
            return True
        i = 0;j = len(num)-1
        while i <= j:
            if num[i] not in mapping or mapping[num[i]] != num[j]:
                return False
            i+=1
            j-=1
        return True

obj = Solution()
print(obj.isStrobogrammatic('00'))