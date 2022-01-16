import queue
class Solution:
    def eliminateMaximum(self, dist, speed):
        zipped = list(zip(dist, speed))
        q = queue.PriorityQueue()
        monsters_killed = 0
        for i, j in zipped:
            q.put([i-j, j])
        while not q.empty():
            d, s = q.get()
            if d <= 0:
                return monsters_killed
            monsters_killed += 1
        return monsters_killed

obj = Solution()
# print(obj.eliminateMaximum([1,3,4], [1,1,1]))
# print(obj.eliminateMaximum([1,1,2,3], [1,1,1,1]))
print(obj.eliminateMaximum([4,3,4], [1,1,2]))



