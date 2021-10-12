class DlinkedList:

    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head, self.tail = DlinkedList(), DlinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def move_to_end(self, node):
        self.remove_node(node)
        self.add_node(node)

    def pop_tail(self):
        curr_tail = self.tail.prev#
        self.remove_node(curr_tail)
        return curr_tail

    def get(self, key):
        node = self.cache.get(key, None)

        if not node:
            return -1
        self.move_to_end(node)
        return node.value

    def put(self, key, value):
        node = self.cache.get(key)

        if not node:
            new = DlinkedList()
            new.key = key
            new.value = value
            self.cache[key] = new
            self.add_node(new)
            self.size += 1

            if self.size > self.capacity:
                tail = self.pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self.move_to_end(node)


### another python solution
from collections import OrderedDict


class LRUCache2(OrderedDict):

    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)

        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value

        if len(self) > self.capacity:
            self.popitem(last=False)
