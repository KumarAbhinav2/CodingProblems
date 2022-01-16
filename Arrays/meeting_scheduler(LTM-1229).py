class Solution:
    def minAvailableDuration(self, slots1, slots2, duration: int):
        for i in slots1:
            for j in slots2:
                if max(i) > min(j):
                    slot = [max(i[0], j[0]), min(i[1], j[1])]
                    if slot[1] - slot[0] >= duration:
                        return [slot[0], slot[0]+duration]
        return []


obj = Solution()
#obj.minAvailableDuration([[0, 2]], [[1, 3]], 1)
obj.minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8)