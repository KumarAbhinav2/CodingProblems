def createTargetArray(nums, index):
    target  = []
    for i in range(len(nums)):
        target.insert(index[i], nums[i])
    return target

createTargetArray([0,1,2,3,4], [0,1,2,2,1])





































# def createTargetArray(nums, index):
#     i = 0
#     target = []
#     while i < len(nums):
#         target.insert(index[i], nums[i])
#         i+=1
#     return target
#
# print(createTargetArray([0,1,2,3,4], [0,1,2,2,1]))
# print(createTargetArray([1,2,3,4,0], [0,1,2,3,0]))
# print(createTargetArray([1], [0]))
#
# def shuffle(nums, n) :
#     i = 0
#     j = n % 2
#     res = []
#     while i < n % 2 and j < n:
#         res += [nums[i], nums[j]]
#         i += 1
#         j += 1
#     return res
#
# shuffle([2,5,1,3,4,7], 3)