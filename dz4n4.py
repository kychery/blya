class FIFO:
    def __init__(self, *args):
        self.queue = []
        for arg in args:
            self.queue.append(arg)

    def __repr__(self):
        return str(self.queue)

    def isEmpty(self):
        if self.queue:
            return False
        else:
            return True

    def push(self, object):
        return self.queue.append(object)

    def pop(self):
        return self.queue.pop(0)



x = FIFO()
j = 12
print(x, x.isEmpty())
for i in range(1, j+1):
    x.push(i)
print(x, x.isEmpty())
x.isEmpty()
for i in range(1, j-5):
    x.pop()
print(x, x.isEmpty())
