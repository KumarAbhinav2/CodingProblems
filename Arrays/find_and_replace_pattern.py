from collections import Counter, defaultdict

class Solution:

    def get_map(self, pattern):
        mmap = defaultdict(list)
        for i, v in enumerate(pattern):
            mmap[v].append(i)
        return mmap

    def findAndReplacePattern(self, words, pattern: str):
        res = []
        p_map = self.get_map(pattern)
        for word in words:
            if len(Counter(word).keys()) != len(p_map):
                continue
            w_map = self.get_map(word)
            p = [v for v in p_map.values()]
            m = [v for v in w_map.values()]
            if p == m:
                res.append(word)
            else:
                continue
        return res

    def findAndReplacePattern_better(self, words, pattern: str):
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True
        return list(filter(match, words))

    # Time: O(N * k) , N = number of words, k=length of each word
    # space: O(N * k)


    def findAndReplacePattern_better2(self, words, pattern: str):
        def match(word):
            p = {}
            for x, y in zip(pattern, word):
                if p.setdefault(x, y) != y:
                    return False
            return len(set(p.values())) == len(p.values())
        return list(filter(match, words))

    # Time: O(N * k) , N = number of words, k=length of each word
    # space: O(N * k)




obj = Solution()
#print(obj.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
#print(obj.findAndReplacePattern_better(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
print(obj.findAndReplacePattern_better2(["abc","deq","mee","aqq","dkd","ccc"], "abb"))