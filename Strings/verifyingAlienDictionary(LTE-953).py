class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        # get the unique character map
        mdict = {c: i for i, c in enumerate(order)}

        def getFirstUnique(w1, w2):
            # no need to traverse from start but only the minimum len string
            for i in range(min(len(w1), len(w2))):
                if w1[i] != w2[i]:
                    if mdict[w1[i]] > mdict[w2[i]]:
                        return False
                    break
            else:
                # if we have unique cases of ["hello", "hello"] or ["apple", "apply"]
                if len(w1) > len(w2):
                    return False
            return True

        for i in range(1, len(words)):
            res = getFirstUnique(words[i - 1], words[i])
            if not res:
                return False
        return True

    # Time Complexity: O(C), c = count of the words
    # Space Complexity: O(1)