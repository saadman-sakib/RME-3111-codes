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


graph = Graph(4)

graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,2)
graph.add_edge(2,0)
graph.add_edge(2,3)
graph.add_edge(3,3)

for i in range(4):
    for j in range(4):
        print(f"path {i} to {j} is {graph.bfs(i, j)}")

