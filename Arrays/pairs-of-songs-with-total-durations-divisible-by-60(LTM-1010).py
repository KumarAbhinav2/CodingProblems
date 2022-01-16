class Solution:
    """
    You are given a list of songs where the ith song has a duration of time[i] seconds.

    Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally,
    we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0
    """

    def brute_force(self, time):
        res = 0
        for i in range(len(time)):
            for j in range(i+1, len(time)):
                if not (time[i]+time[j]) % 60:
                    res += 1
        return res

    # Time complexity: O(n**2)
    # Space complexity: O(1)

    def better(self, time):
        res = 0
        rem = [0]*60
        for t in time:
            if t % 60 == 0:
                res += rem[0]
            else:
                res += rem[60 - t%60]
            rem[t%60] += 1
        return res

    # Time complexity: O(n)
    # Space complexity: O(1)

    def better2(self, time):
        res = 0
        dp = [0]*60
        for t in time:
            rem = t%60
            target = (60 - rem) % 60
            res += dp[target]
            dp[rem] += 1
        return res

    # Time complexity: O(n)
    # Space complexity: O(1)