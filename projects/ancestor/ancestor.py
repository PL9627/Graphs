from util import Stack, Queue
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    """ graph = Graph()

    for ancestor in ancestors:
        graph.add_vertex(ancestor[0])
        graph.add_vertex(ancestor[1])
        graph.add_edge(ancestor[1], ancestor[0])

    stack = Stack()
    stack.push([starting_node])

    max_path = 1
    early_A = -1

    while stack.size() > 0:
        path = stack.pop()
        curr = path[-1]

        if len(path) > max_path:
            max_path = len(path)
            early_A = curr

        neighbor = graph.get_neighbors(curr)

        for pair in neighbor:
            copyPath = list(path)
            copyPath.append(pair)
            stack.push(copyPath)

    return early_A """

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
