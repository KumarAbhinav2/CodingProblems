"""
Given an array of integers arr of even length n and an integer k.
We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
"""

class Solution:
    def canArrange(self, arr, k):
        # array to hold pairs
        count = [0] * k
        for num in arr:
            count[num%k] += 1
        for i in range(k):
            # because we know as given condition (i + j) % k == 0
            j = -i % k
            while count[i] > 0:
                count[i] -=1
                count[j] -=1
                # decrementing both the pairs from the array
                if count[j] < 0:
                    # if we don't have pair
                    return False
        return True

    def canArrange_better(self, arr, k):
        # array to hold pairs
        count = [0] * k
        for num in arr:
            count[num%k] += 1
        if count[0] % 2: return False
        i, j = 1, k-1
        while i < j:
            if count[i] != count[j]:
                return False
            i+=1
            j-=1
        return True


# Time Complexity: O(n)
# Space Complexity: O(k)


