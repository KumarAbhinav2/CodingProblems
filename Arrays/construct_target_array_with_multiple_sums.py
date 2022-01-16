import heapq
class Solution:
    def isPossible(self, target) -> bool:
        if len(target) == 1:
            return target == [1]
        heap = []
        total_sum = sum(target)
        target_map = {v:i for i,v in enumerate(target)}
        heapq.heapify(target)
        while heap:
            max_val, max_index = heapq.heappop(heap)
            rest_sum = total_sum-abs(max_val)
            total_sum = abs(max_val)
            target_map[abs(max_val)] = abs(abs(max_val)-rest_sum)
            if target_map[abs(max_val)] > 1:
                heapq.heappush(heap, [-target_map[abs(max_val)], max_index])
            elif target_map[abs(max_val)] < 1:
                return False
        return True

obj = Solution()
#print(obj.isPossible([9,3,5]))
#print(obj.isPossible([1,1,1,2]))
#print(obj.isPossible([1,1000000000]))
print(obj.isPossible([4]))