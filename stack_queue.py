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


class Stack:
    def __init__(self):
        self.top: Node = None

    def push(self, node: Node):
        node.parent = self.top
        if self.top != None:
            self.top.child = node
        self.top = node

    def pop(self):
        popped_node = self.top
        self.top = self.top.parent
        if self.top != None:
            self.top.child = None
        return popped_node

    def is_empty(self):
        return self.top == None


class Queue:
    def __init__(self):
        self.front: Node = None
        self.back: Node = None

    def push(self, node: Node):
        node.parent = self.back
        if self.back != None:
            self.back.child = node
        self.back = node
        if self.front == None:
            self.front = node

    def pop(self):
        popped_node = self.front
        self.front = self.front.child
        if self.front != None:
            self.front.parent = None
        if self.front == None:
            self.back = None
        return popped_node

    def is_empty(self):
        return self.back == None and self.front == None


def stack_driver():
    stack = Stack()
    x = [4, 7, 9, 1, 3, 0, 12]

    for a in x:
        node = Node(a)
        stack.push(node)

    while not stack.is_empty():
        print(stack.pop())


def queue_driver():
    queue = Queue()
    x = [4, 7, 9, 1, 3, 0, 12]

    for a in x:
        node = Node(a)
        queue.push(node)

    while not queue.is_empty():
        print(queue.pop())


if __name__ == '__main__':
    print("===========Running Stack Test============")
    stack_driver()
    print("===========Running Queue Test==============")
    queue_driver()
