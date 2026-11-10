class MyQueue:

    def __init__(self):
        self.stack=[]
        self.myQueue=[]

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.myQueue.pop()

    def peek(self) -> int:
        if not self.myQueue:
            while self.stack:
                self.myQueue.append(self.stack.pop())
        return self.myQueue[-1]

    def empty(self) -> bool:
        return not self.stack and not self.myQueue


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()