
class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.pushLeft(root)

    def pushLeft(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        node = self.stack.pop()

        if node.right:
            self.pushLeft(node.right)

        return node.val

    def hasNext(self):
        return len(self.stack) > 0
