"""
Convert a given number into correct roman equivalent

Eg: input: 67
    output: LXVII
"""

class Solution:
    def intToRoman(self, num):
        res = ''
        ref = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90),
              ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]
        for s, val in ref:
            if not num:
                break
            if num < val:
                continue
            else:
                t = int(num/val)
                num = num-(t*val)
                res += s*t
        return res