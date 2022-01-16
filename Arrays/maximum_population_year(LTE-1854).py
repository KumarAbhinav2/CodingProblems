from collections import Counter
import heapq
class Solution:
    def maximumPopulation(self, logs) -> int:
        arr = []
        for i in logs:
            arr.extend(list(range(i[0], i[1])))
        c_arr = Counter(arr)
        res = sorted(c_arr.items(), key=lambda x:(x[1]), reverse=True)
        max_arr = []
        if len(arr) == 1:
            return arr[0]
        for i in range(1, len(res)):
            if res[i][1] == res[i-1][1]:
                heapq.heappush(max_arr, res[i-1][0])
            else:
                heapq.heappush(max_arr, res[i-1][0])
                break
        return heapq.heappop(max_arr)

    def maximumPopulation2(self, logs) -> int:
        pop = [0]*2051
        for b,d in logs:
            while b < d:
                pop[b]+=1
                b+=1
        return pop.index(max(pop))



obj  = Solution()
print(obj.maximumPopulation([[1950,1961],[1960,1971],[1970,1981]]))
print(obj.maximumPopulation([[1993,1999],[2000,2010]]))
print(obj.maximumPopulation([[1993,1994]]))
print(obj.maximumPopulation([[1945, 2021], [1950,1961],[1960,1971],[1970,1981], [1985, 2054]]))
print(obj.maximumPopulation([[2033,2034],[2039,2047],[1998,2042],[2047,2048],[2025,2029],[2005,2044],[1990,1992],[1952,1956],[1984,2014]]))