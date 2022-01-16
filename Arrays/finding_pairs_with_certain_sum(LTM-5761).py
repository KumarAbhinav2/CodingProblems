import collections
class FindSumPairs:

    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.lk = collections.defaultdict(list)
        self.hmap = self.init_hash()


    def init_hash(self):
        hmap = collections.defaultdict(list)
        for i, iv in enumerate(self.nums1):
            for j, jv in enumerate(self.nums2):
                self.lk[j].append(iv+jv)
                hmap[iv+jv].append((i, j))
        return hmap

    def update_hash(self, index, val):
        vals = set(self.lk[index])
        for v in vals:
            old = self.hmap[v+val]
            new = self.hmap[v]
            up = set(old+new)
            self.hmap[v+val] = list(up)
            uv = [i for i in self.hmap[v] if i[1] != index]
            self.hmap[v] = uv

    def add(self, index: int, val: int) -> None:
        self.nums2[index]+=val
        self.update_hash(index, val)

    def count(self, tot: int) -> int:
        return len(self.hmap[tot])

obj = FindSumPairs([1, 1, 2, 2,2, 3], [1, 4, 5, 2, 5, 4])
print(obj.count(7))
print(obj.add(3,2))
print(obj.count(8))
print(obj.count(4))
print(obj.add(0,1))
print(obj.add(1,1))
print(obj.count(7))
