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
        return self.g == other.g
    
    def __gt__(self, other):
        return self.g > other.g
    
    def __lt__(self, other):
        return self.g < other.g
    
    def __str__(self) -> str:
        return f"Node:{self.value}"
    
    def __repr__(self) -> str:
        return f"Node:{self.value}"


n1 = Node("s")
n1.g = 3

n2 = Node("r")
n2.g = 5

print(n1 > n2)