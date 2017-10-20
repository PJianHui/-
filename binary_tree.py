class Tree(object):
    def __init__(self, element=None):
        self.element = element
        self.left = None
        self.right = None

    def traversal(self):
        # 递归,先序遍历
        print(self.element)
        if self.left is not None:
            self.left.traversal()
        if self.right is not None:
            self.right.traversal()

    def reverse(self):
        # 递归翻转
        self.left, self.right = self.right, self.left
        if self.left is not None:
            self.left.reverse()
        if self.right is not None:
            self.right.reverse()


def test():
    t = Tree(0)
    t.left = Tree(1)
    t.right = Tree(2)
    t.traversal()
    t.reverse()
    t.traversal()

if __name__ =='__main__':
    test()