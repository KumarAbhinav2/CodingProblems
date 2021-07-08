class Solution:
    def maxProduct(self, words):
        max_len = 0
        while words:
            elem = words.pop()
            l = len(elem)
            for word in words:
                common = set(word).intersection(set(elem))
                if not common:
                    max_len = max(max_len, len(word)*l)
        return max_len


    def no_common_letters(self, s1, s2):
        bitnumber = lambda x: ord(x) - ord('a')

        b1 = b2 = 0
        for ch in s1:
            bn = bitnumber(ch)
            b1 |= 1 << bn
        for ch in s2:
            bn = bitnumber(ch)
            b2 |= 1 << bn
        return b1 & b2 == 0

    def maxProduct2(self, words):
        n = len(words)
        masks = [0]*n
        lens = [0]*n
        bit_number = lambda x: ord(x) - ord('a')

        for i in range(n):
            bitmask = 0
            for ch in words[i]:
                bitmask |= 1 << bit_number(ch)
            masks[i] = bitmask
            lens[i] = len(words[i])

        max_val = 0
        for i in range(n):
            for j in range(i+1, n):
                if masks[i] & masks[j] == 0:
                    max_val = max(max_val, len(words[i])*len(words[j]))
        return max_val








obj = Solution()
print(obj.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
print(obj.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
print(obj.maxProduct(["a","aa","aaa","aaaa"]))