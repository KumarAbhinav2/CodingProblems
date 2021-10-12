"""Graph implementation using linked list"""


class AdjacentNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        if not self.head:
            return True
        return False

    def insert_at_head(self, data):
        new_node = AdjacentNode(data)
        if self.is_empty():
            self.head = new_node
            return self.head
        new_node.next = self.head
        self.head = new_node
        return self.head


class Graph:
    """Directed"""
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        for i in range(vertices):
            temp = LinkedList()
            self.graph.append(temp)

    def add_edge(self, src, dest):
        if src < self.vertices and dest < self.vertices:
            self.graph[src].insert_at_head(dest)

    def print_graph(self):
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.graph[i].get_head()
            while temp is not None:
                print("[", temp.val, end=" ] -> ")
                temp = temp.next
            print('None')


if __name__ == '__main__':
    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.print_graph()




