import queue
class Solution:
    def closestRoom_TLE(self, rooms, queries):
        ans = []
        pq = queue.PriorityQueue()
        for i in queries:
            for j in rooms:
                a = abs(i[0] - j[0])
                pq.put((a, j))
            while not pq.empty():
                top = pq.get()
                if top[1][1]>=i[1]:
                    ans.append(top[1][0])
                    break
            else:
                ans.append(-1)
        return ans if ans else -1

    def closestRoom_Working(self, rooms, queries):
        import bisect
        ans = [None]*len(queries)
        rooms.sort(reverse=True, key=lambda x:(x[1], x[0]))
        queries = sorted([(s, p, i) for i, (p, s) in enumerate(queries)], reverse=True)
        rms = [-1]
        j = 0
        for s, p, i in queries:
            while j < len(rooms) and rooms[j][1] >= s:
                bisect.insort(rms, rooms[j][0])
                j+=1
            x = bisect.bisect_left(rms, p)
            #ans[i] = rms[x - 1] if (x == len(rms) or x != 1 and abs( rms[x - 1] - p) <= abs(rms[x] - p)) else rms[x]
            if (x == len(rms) or x != 1 and abs( rms[x - 1] - p) <= abs(rms[x] - p)):
                ans[i] = rms[x - 1]
            else:
                ans[i] = rms[x]

        return ans


obj = Solution()
print(obj.closestRoom_Working([[2,2],[1,2],[3,2]], [[3,1],[3,3],[5,2]]))
#print(obj.closestRoom([[1,4],[2,3],[3,5],[4,1],[5,2]], [[2,3],[2,4],[2,5]]))