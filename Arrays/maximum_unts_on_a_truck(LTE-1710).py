class Solution:
    def maximumUnits(self, boxTypes, truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        csize = 0
        i = 0
        res = 0
        while csize < truckSize:
            csize += boxTypes[i][0]
            if csize > truckSize:
                last_one = (boxTypes[i][0] - (csize-truckSize))*boxTypes[i][1]
                res+=last_one
            else:
                res+=(boxTypes[i][0]*boxTypes[i][1])
            i+=1
        return res

obj  =Solution()
obj.maximumUnits([[1,3],[2,2],[3,1]], 4)