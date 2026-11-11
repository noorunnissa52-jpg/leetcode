
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index):
        curr = self.head

        for i in range(index):
            if curr is None:
                return -1
            curr = curr.next

        if curr is None:
            return -1
        return curr.val

    def addAtHead(self, val):
        new = Node(val)
        new.next = self.head
        self.head = new

    def addAtTail(self, val):
        new = Node(val)

        if self.head is None:
            self.head = new
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new

    def addAtIndex(self, index, val):
        if index <= 0:
            self.addAtHead(val)
            return

        curr = self.head

        for i in range(index - 1):
            if curr is None:
                return
            curr = curr.next

        if curr is None:
            return

        new = Node(val)
        new.next = curr.next
        curr.next = new

    def deleteAtIndex(self, index):
        if index < 0 or self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head

        for i in range(index - 1):
            if curr is None:
                return
            curr = curr.next

        if curr is None or curr.next is None:
            return

        curr.next = curr.next.next
