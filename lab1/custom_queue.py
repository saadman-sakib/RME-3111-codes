class Node:
    def __init__(self, value, parent=None, child=None):
        self.parent = parent  # parent node
        self.value = value   # value of the current node
        self.child = child  # child node

    def __repr__(self) -> str:
        if self.parent:
            parent = self.parent.value
        else:
            parent = None

        if self.child:
            child = self.child.value
        else:
            child = None

        return f"------\n value:{self.value} \n parent:{parent} \n child:{child}\n -------\n\n"

    def __str__(self) -> str:
        if self.parent:
            parent = self.parent.value
        else:
            parent = None

        if self.child:
            child = self.child.value
        else:
            child = None

        return f" ---Node---\n value:{self.value} \n parent:{parent} \n child:{child}\n -----------\n"


class Queue:
    def __init__(self):
        self.front: Node = None
        self.back: Node = None

    def push(self, node: Node)->None:
        node.parent = self.back
        if self.back != None:
            self.back.child = node
        self.back = node
        if self.front == None:
            self.front = node

    def pop(self)->Node:
        popped_node = self.front
        self.front = self.front.child
        if self.front != None:
            self.front.parent = None
        if self.front == None:
            self.back = None
        return popped_node

    def is_empty(self)->bool:
        return self.back == None and self.front == None
