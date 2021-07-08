"""
Convert a given roman string to integer

Eg: input: "IV"
    output: 4
"""

class Solution:
    def romanToInt(self, s):
        rvmap = {
            "I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000
        }
        res = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and rvmap[s[i]] < rvmap[s[i+1]]:
                res += (rvmap[s[i+1]] - rvmap[s[i]])
                i+=2
            else:
                res += rvmap[s[i]]
                i+=1
        return res