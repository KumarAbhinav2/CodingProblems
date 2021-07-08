class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones = 0
        zero = 0
        longest_ones = 0
        longest_zeros = 0
        for i in s:
            if i == '1':
                zero = 0
                ones+=1
            else:
                ones = 0
                zero += 1
            longest_ones = max(longest_ones, ones)
            longest_zeros = max(longest_zeros, zero)
        return longest_ones > longest_zeros

obj = Solution()
print(obj.checkZeroOnes("1101"))
print(obj.checkZeroOnes("111000"))
print(obj.checkZeroOnes("110100010"))