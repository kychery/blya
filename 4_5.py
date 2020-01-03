class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Litterlist:
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'Litterlist: '+str(current.value)
            while current.next is not None:
                current = current.next
                out += ', ' + str(current.value)
            return out
        return 'Litterlist is Empty'

    def clear(self):
        self.__init__()

    def append(self, x):
        if self.first is None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current



L = Litterlist()
L.append(1)
L.append(124)
L.clear()
L.append(12)
L.append(45)
print(L)
