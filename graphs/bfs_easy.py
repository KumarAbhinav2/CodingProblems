"""
Implement BFS on given graph
"""
g = {
    1: [2, 3],
    2:[4, 5],
    3:[6, 7],
    4:[],
    5:[],
    6:[],
    7:[]
}


def bfs(root):
    if not root:
        return
    queue = [root]
    visited = []
    while queue:
        node = queue.pop(0)
        print(node)
        visited.append(root)
        for n in g[node]:
            if n in visited:
                continue
            else:
                queue.append(n)


def dfs(root):
    if not root:
        return
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        print(node)
        visited.append(root)
        for n in g[node]:
            dfs(n)


bfs(1)
print("#####################")
dfs(1)


