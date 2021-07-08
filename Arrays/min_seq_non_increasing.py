

def minSubsequence(nums):
    s = sorted(nums, reverse = True)
    new_list = []
    Sum = 0
    Limit = sum(nums ) /2
    for i in range(len(s)):
        new_list.append(s[i])
        Sum += s[i]
        if Sum > Limit:
            return new_list

minSubsequence([4,3,10,9,8])