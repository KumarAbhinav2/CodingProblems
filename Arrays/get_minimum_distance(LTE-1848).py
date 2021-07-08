import queue
class Solution:
    def getMinDistance_intuitive(self, nums, target: int, start: int) -> int:
        if not start:
            i = nums.index(target)
            return abs(i-start)
        heap = queue.PriorityQueue()
        for i in range(len(nums)):
            if nums[i] == target:
                heap.put((abs(i-start), i))
        item = heap.get()
        return abs(item[0])

    def getMinDistance(self, nums, target: int, start: int) -> int:
        filtered = [i for i in range(len(nums)) if nums[i] == target]
        return min(abs(i-start) for i in filtered)


obj = Solution()
print(obj.getMinDistance([1,2,3,4,5], 5, 3))
print(obj.getMinDistance([1], 1, 0))
print(obj.getMinDistance([1,1,1,1,1,1,1,1,1,1], 1, 0))
print(obj.getMinDistance([1,1,1,1,1,1,1,1,1,1], 1, 9))
print(obj.getMinDistance([5,3,6], 5, 2))
print(obj.getMinDistance([1,5,3,4,5], 5, 2))

