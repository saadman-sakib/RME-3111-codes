from heap import Heap


class Node:
    def __init__(self, value):
        self.value = value
        self.h = 0
        self.g = 0
        self.f_n = 0
        self. parent = None

    def update_f_n(self, g_n, h_n, parent):
        self.g = g_n
        self.h = h_n
        self.f_n = g_n + h_n
        self.parent = parent

    def __hash__(self) -> int:
        return hash(self.value)
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __str__(self) -> str:
        return f"Node:{self.value}"
    
    def __repr__(self) -> str:
        return f"Node:{self.value}"


class Edge:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight
    
    def __str__(self) -> str:
        return f"Edge:{self.destination.value}-{self.weight}"

    def __repr__(self) -> str:
        return f"Edge:{self.destination.value}-{self.weight}"


class PriorityQueue(Heap):
    def compare(self, a:Node, b:Node):
        return a.f_n > b.f_n


class Graph:
    def __init__(self, size):
        self.size = size
        self.adj_list = dict()
        self.path_cost = dict()
        self.huristic = dict()
        self.parent = dict()


    def add_edge(self, source:Node, destination:Edge):
        if source not in self.adj_list:
            self.adj_list[source] = []
        self.adj_list[source].append(destination)
    
    def astar(self, source:Node, destination:Node):
        mark = set()
        queue = PriorityQueue()
        queue.push(source)

        while not queue.is_empty():
            node = queue.pop()
            mark.add(node)
            self.path_cost[node] = node.g
            self.parent[node] = node.parent
            if node.value == destination.value:
                return True
            for edge in self.adj_list[node]:
                if edge.destination not in mark:
                    edge.destination.update_f_n(self.path_cost[node]+edge.weight, 
                                                self.huristic[edge.destination.value], 
                                                node)
                    queue.push(edge.destination)
        return False

    def print_path(self, source:Node, destination:Node):
        if self.astar(source, destination):
            path = []
            node = destination
            while node != source:
                path.append(node.value)
                node = self.parent[node]
            path.append(source.value)
            path.reverse()
            print(path)
        else:
            print("No path found")


if __name__ == "__main__":
    graph_dict = {
        "s": [("a", 2), ("b", 4)],
        "a": [("b", 1), ("c", 4)],
        "b": [("c", 2), ("g", 6)],
        "c": [("g", 3)],
        "g": [],
    }
    graph = Graph(5)
    for key, value in graph_dict.items():
        for dest, weight in value:
            graph.add_edge(Node(key), Edge(Node(dest), weight))
    graph.huristic = {
        "s": 7,
        "a": 4,
        "b": 5,
        "c": 2,
        "g": 0,
    }
    
    graph.print_path(Node("s"), Node("g"))
