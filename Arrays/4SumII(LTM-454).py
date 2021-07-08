class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
                d = {}
                res = 0
                for i in A:
                    for j in B:
                        d[i+j] = d.get(i+j, 0)+1

                for i in C:
                    for j in D:
                        res += d.get(-i-j, 0)
                return res

    def fourSumCount2(self, A, B, C, D):
        import collections
        AB = collections.Counter(a + b for a in A for b in B)
        return sum(AB[-c - d] for c in C for d in D)

    # Time: O(N*N)
    # Spaec: O(N*N)

