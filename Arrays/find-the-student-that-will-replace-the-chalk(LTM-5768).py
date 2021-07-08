class Solution:
    def chalkReplacer(self, chalk, k: int):
        c_sum = sum(chalk)
        # get the remainder we only have to iterate though it
        _, rem = divmod(k, c_sum)
        i = 0
        while rem > 0:
            rem -= chalk[i]
            # student with less chalk than expected
            if rem < 0:
                return i
            i+=1
        return i



obj = Solution()
print(obj.chalkReplacer([5,1,5], 22))
print(obj.chalkReplacer([3,4,1,2], 25))
print(obj.chalkReplacer([30,76,46,74,34,12,1,82,25,28,63,29,60,76,98,20,40,32,76,26,71], 346237330))
