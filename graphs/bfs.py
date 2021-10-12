"""
Implementing BFS
step1: We will receive a starting node or we have to select 1
step2: Take an empty queue to store current exploring vertex and a list to keep hold of visited ones
step3: Visit the source vertex , add it to the queue and update visited
"""
from graph_implementation_ll import Graph, LinkedList, AdjacentNode
from graph import Queue

def _traverse(g, source, visited):
    result = ''
    queue = Queue()
    queue.enqeue(source)
    visited.add(source)
    while not queue.isEmpty():
        vertex = queue.dequeue()
        result += str(vertex)
        curr_node = g.graph[source].get_head()
        while curr_node is not None:
            if curr_node.val not in visited:
                queue.enqeue(curr_node.val)
                visited.add(curr_node.val)
            curr_node = curr_node.next
    return result, visited


def bfs_traversal(graph_obj, source):
    result = ""
    no_of_vertices = graph_obj.vertices
    if not no_of_vertices: return result
    visited = set()
    result, visited = _traverse(graph_obj, source, visited)
    for i in range(no_of_vertices):
        if i in visited:
            result_new, visited = _traverse(g, i, visited)
            result += result_new
    return result

g = Graph(4)
num_of_vertices = g.vertices

if(num_of_vertices is 0):
    print("Graph is empty")
elif(num_of_vertices < 0):
    print("Graph cannot have negative vertices")
else:
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.print_graph()
    print(bfs_traversal(g, 0))



