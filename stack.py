#简单的栈实现
#往head添加新元素


class Node():
    def __init__(self, element=None, next=None):
        self.element =element
        self.next = next

    # print 的时候调用
    def __repr__(self):
        return str(self.element)


class Stack():
    def __init__(self):
        self.head = Node()

    # next 为 None， 空栈
    def is_empty(self):
        return self.head.next is None

    # 创建一个node，并让它指向当前head.next指向的元素，再把head.next指向它，
    def push(self, element):
        self.head.next = Node(element, self.head.next)

    #取出元素
    def pop(self):
        node = self.head.next
        print(node.next)
        # 找到第一个元素， 该元素 next 属性为 None,
        if not self.is_empty():
            self.head.next = node.next
        return node

    # head.next是栈里的第一个元素
    def top(self):
        return self.head.next


def test():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())


if __name__ == '__main__':
    test()

