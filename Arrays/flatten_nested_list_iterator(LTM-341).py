class NestedIterator:
    def __init__(self, nestedList):
        self.list = self._flatten(nestedList)
        self.pos = -1

    def _flatten(self, nlist):
        ll = []
        for elem in nlist:
            if elem.isInteger():
                ll.append(elem.getInteger())
            else:
                ll.extend(self._flatten(elem.getList()))
        return ll

    def next(self) -> int:
        self.pos += 1
        return self.list[self.pos]

    def hasNext(self) -> bool:
        return self.pos < len(self.list) - 1
