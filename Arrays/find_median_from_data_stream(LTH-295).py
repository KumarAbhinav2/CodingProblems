from heapq import *
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        if len(self.small) == len(self.large):
            elem = -heappushpop(self.small, -num)
            heappush(self.large, elem)
        else:
            elem = -heappushpop(self.large, num)
            heappush(self.small, elem)

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0])/2.0
        else:
            return float(self.large[0])


obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.findMedian()