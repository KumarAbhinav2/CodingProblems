import heapq
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    dp[t + 1] = max(dp[t + 1], dp[t] + capacity)

        for i, d in enumerate(dp):
            if d >= target: return i
        return -1

    # Time: O(N**2)
    # Space: O(N)

    def minRefuelStops2(self, target: int, startFuel: int, stations) -> int:
        pq = []
        ans = prev = 0
        stations.append([target, float('inf')])
        for location,capacity in stations:
            startFuel -= location - prev
            while pq and startFuel < 0:
                startFuel += -heapq.heappop(pq)
                ans+=1
            if startFuel < 0: return -1
            heapq.heappush(pq, -capacity)
            prev = location
        return ans

    # Time: O(NlogN)
    # Space: O(N)

obj = Solution()
obj.minRefuelStops(100, 10, [[10, 20], [20, 30], [30, 30], [60, 40]])