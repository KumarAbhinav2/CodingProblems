from collections import defaultdict

class Graph:

    def __init__(self, directed = False):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, source, destination):
        self.graph[source].append(destination)
        if not self.directed:
            self.graph[destination].append(source)

    def print_graph(self):
        for source, destinations in self.graph.items():
            print(source , "->", destinations)
        print(self.graph)

def bfs_traversal(g, source):
    result = ''
    visited = []
    queue = []
    visited.append(source)
    queue.append(source)
    while queue:
        vertex = queue.pop(0)
        result += str(vertex)
        for i in g.graph[vertex]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return result

def dfs(g, source):
    visited = set()    # 'in' operation in set is faster than list
    visited.add(source)
    for node in g.graph:
        if node not in visited:
            dfs(g, node)



def dfs_without_recursion(graph, node):
    visited = [node]
    stack = [node]
    while stack:
        node = stack[-1]
        if node not in visited:
            visited.append(node)
        remove_from_stack = True
        for next in graph[node]:
            if next not in visited:
                stack.append(next)
                remove_from_stack = False
                break
        if remove_from_stack:
            stack.pop()
    return visited


g = Graph(directed=True)
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.print_graph()
bfs_traversal(g, 'A')
print(dfs(g.graph, 'A'))

