# https://leetcode.com/problems/implement-stack-using-queues/description/
from queue import Queue


class MyStack:

    def __init__(self):
        self.q1 =Queue()
        self.q2 =Queue()
        

    def push(self, x: int) -> None:
        self.q1.put(x)
        

    def pop(self) -> int:
       while not self.q1.empty():
           if self.q1.qsize()==1:
                var = self.q1.get()
                while not self.q2.empty():
                    self.q1.put(self.q2.get())
                return var
           else:
                self.q2.put(self.q1.get())
           
            

    def top(self) -> int:
        while not self.q1.empty():
            if self.q1.qsize()==1:
                var = self.q1.get()
                self.q2.put(var)
                while not self.q2.empty():
                    self.q1.put(self.q2.get())
                return var
            else:
                self.q2.put(self.q1.get())
        

        

    def empty(self) -> bool:
        return True if self.q1.empty() else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()