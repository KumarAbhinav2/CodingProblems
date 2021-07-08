class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(' ')
        mmp = [0]*(len(s)+1)
        for word in s:
            mmp[int(word[-1])] = word[:-1]
        return ' '.join(mmp[1:])


obj = Solution()
print(obj.sortSentence("is2 sentence4 This1 a3"))
print(obj.sortSentence("Myself2 Me1 I4 and3"))