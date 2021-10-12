graph = {
    0: [2, 3],
    2: [3],
    3: [],
    4: [5],
    5: [6],
    6: [4]
}

white = set()  # will host unvisited nodes
grey = set()  # will host visiting nodes
black = set()  # will host visited nodes/ completed nodes
path_map = set()
parent = None

white = set(graph.keys())

def detectCycle(graph, source, parent):

    if source in grey:
        print("Found cycle")
        return True
    elif source in black:
        return True

    grey.add(source)
    path_map.add((parent, source))

    for neighbour in graph[source]:
        detectCycle(graph, neighbour, source)
    grey.remove(source)
    black.add(source)





