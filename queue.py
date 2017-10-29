class Node():
    def __init__(self, element=None, next=None):
        self.element = element
        self.next = next

    def __repr__(self):
        return str(self.element)

# 新进来的元素往 tail 添加


class Queue():
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def empty(self):
        return self.head.next is None

    # 入队，
    def enqueue(self, element):
        node = Node(element)
        #让目前的tail.next指向node
        self.tail.next = node
        #新的tail就是node，新的node.next还是none
        self.tail = node

    def dequeue(self):
        node = self.head.next
        if not self.empty():
            self.head.next = node.next
        return node


def test():
    q = Queue()

    q.enqueue(1)
    # print(q.head, q.tail)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    # print(q.head, q.tail)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

if __name__ == '__main__':
    test()