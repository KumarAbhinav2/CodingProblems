class Solution:
    def maxBoxesInWarehouse(self, boxes, warehouse):
        boxes.sort(reverse=True)
        no_of_boxes = 0
        i, j = 0, 0

        while warehouse and boxes:
            box = boxes.pop()
            while j <= len(warehouse)-1 and warehouse[j] >= box:
                    j+=1
            if j:
                no_of_boxes+=1
                warehouse = warehouse[:j - 1]
            else:
                break
            j = 0

        return no_of_boxes

obj = Solution()
print(obj.maxBoxesInWarehouse([4,3,4,1], [5,3,3,4,1]))
print(obj.maxBoxesInWarehouse([1,2,2,3,4], [3,4,1,2]))
print(obj.maxBoxesInWarehouse([1,2,3], [1,2,3,4]))
print(obj.maxBoxesInWarehouse([4,5,6], [3,3,3,3,3]))

