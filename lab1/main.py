from custom_queue import Queue, Node

class Graph:
    def __init__(self, size):
        self.size = size
        self.adj_list = [[]for i in range(size)]

    def add_edge(self, source, destination):
        self.adj_list[source].append(destination)
    
    def bfs(self, source, destination):
        mark = [False for i in range(self.size)]
        queue = Queue()
        queue.push(Node(source))

        while not queue.is_empty():
            node = queue.pop().value
            for x in self.adj_list[node]:
                if x==destination:
                    return True
                if mark[x] != True:
                    queue.push(Node(x))
                    mark[x] = True
        return False


with open("input.txt", "r") as f:
    nv, ne, _ =  map(int, f.readline().split()) # number of vertices, edges
    graph = Graph(nv)

    for i in range(ne):
        u, v = map(int, f.readline().split())
        graph.add_edge(u, v)
    
    nq = int(f.readline()) # number of queries

    for i in range(nq):
        s, d = map(int, f.readline().split())
        if(graph.bfs(s, d)):
            print(f"path exists from {s} to {d}")
        else:
            print(f"No path exits from {s} to {d}")

