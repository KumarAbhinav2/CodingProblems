

class Solution:

    def toh(self, n, from_rod, to_rod, aux_rod):
        if n >= 1:
            self.toh(n-1, from_rod, aux_rod, to_rod)
            print("Move disk", n, "From",from_rod,"to", to_rod)
            self.toh(n-1, aux_rod, to_rod, from_rod)


n = 4
s = Solution()
s.toh(n,'A','B','C')


