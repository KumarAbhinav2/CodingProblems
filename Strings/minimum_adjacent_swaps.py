import heapq
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        i = len(num)-2
        j = len(num)
        heap = []
        d = {}
        count = 0
        while i>=0 and j >=0:
            wind = num[i:j]
            if int(wind[::-1]) > int(wind):
                count+=1
                num = num.replace(num[i:j], wind[::-1])
                d[num] = count
                heapq.heappush(heap, int(num))
                i = len(num)-2
                j = len(num)
            else:
                i-=1
                j-=1
        return heapq.nsmallest(k, heap)
        # while k:
        #     elem = heapq.heappop(heap)
        #     k-=1
        # return elem

obj = Solution()
print(obj.getMinSwaps("5489355142", 4))
# print(obj.getMinSwaps("11112", 4))
# print(obj.getMinSwaps("00123", 1))

