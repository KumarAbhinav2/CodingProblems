class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str):
        r = "abcdefghijklmnopqrstuvwxyz"
        i_map = {v:i for i, v in enumerate(r)}
        n1 = ''
        for w in firstWord:
            n1+=str(i_map[w])
        n1 = int(n1)
        n2 = ''
        for w in secondWord:
            n2+=str(i_map[w])
        n2 = int(n2)
        n3 = ''
        for w in targetWord:
            n3+=str(i_map[w])
        n3 = int(n3)
        return (n1+n2) == n3

obj = Solution()
print(obj.isSumEqual("acb", "cba", "cdb"))
print(obj.isSumEqual("aaa", "a", "aab"))
print(obj.isSumEqual("aaa", "a", "aaaa"))

