from util import Stack, Queue
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for ancestor in ancestors:
        parent = ancestor[0]
        chile = ancestor[1]

    """ for ancestor in ancestors:
        graph.add_vertex(ancestor[0])
        graph.add_vertex(ancestor[1])
        graph.add_edge(ancestor[1], ancestor[0])

    queue = Queue()
    queue.enqueue([starting_node])

    long_path = 1
    early = -1

    while queue.size() > 0:
        path = queue.dequeue()
        v = path[-1]
        if(len(path) >= long_path and v < early) or (len(path) > long_path):
            early = v
            long_path = len(path)
        for i in graph.vertices[v]:
            prev_a = list(path)
            prev_a.append(i)
            queue.enqueue(prev_a)
    return early """
