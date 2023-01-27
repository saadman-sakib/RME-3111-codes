class Heap:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def compare(self, a, b):
        raise NotImplementedError

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def get_parent(self, i):
        return int((i-1)/2)

    def get_left_child(self, i):
        return 2*i+1

    def get_right_child(self, i):
        return 2*i+2

    def get_max_pos(self, i, j):
        if(i > len(self.items)-1):
            return j
        elif(j > len(self.items)-1):
            return i
        else:
            return j if self.compare(i, j) else i

    def reheap_up(self):
        size = len(self.items)
        i = size-1
        while i > 0:
            p = self.get_parent(i)
            if (self.compare(p, i)):
                self.swap(i, p)
                i = p
            else:
                break

    def reheap_down(self):
        size = len(self.items)
        i = 0
        while i < size:
            left = self.get_left_child(i)
            right = self.get_right_child(i)
            new_ind = self.get_max_pos(left, right)
            if (new_ind < size and self.compare(i, new_ind)):
                self.swap(i, new_ind)
                i = new_ind
            else:
                break

    def push(self, value):
        self.items.append(value)
        self.reheap_up()

    def pop(self):
        if(self.size()<0):
            return -1
        self.swap(0, -1)
        to_pop = self.items.pop()
        self.reheap_down()
        return to_pop


class MaxHeap(Heap):
    def compare(self, a, b):
        return self.items[a] < self.items[b]


class MinHeap(Heap):
    def compare(self, a, b):
        return self.items[a] > self.items[b]


def heapsort_ascending(l:list):
    heap = MinHeap()
    for x in l:
        heap.push(x)
    
    new_l = []
    for _ in range(len(l)):
        new_l.append(heap.pop())
    
    return new_l

def heapsort_decending(l:list):
    heap = MaxHeap()
    for x in l:
        heap.push(x)
    
    new_l = []
    for _ in range(len(l)):
        new_l.append(heap.pop())
    
    return new_l


if __name__ == '__main__':
    my_list = [12,43,5,1,5,67,123,34,5,67,8,10,12,14,2,9]
    new_list = heapsort_ascending(my_list)
    print("ascending:", new_list)
    new_list = heapsort_decending(my_list)
    print("decending:", new_list)
