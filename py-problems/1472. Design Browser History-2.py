# https://leetcode.com/problems/design-browser-history/description/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.enque=[]
        self.deque=[]
        self.visit(homepage)


    def visit(self, url: str) -> None:
        self.enque.append(url)
        self.deque =[]
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if len(self.enque)==1:
                return self.enque[-1]
            else:
                self.deque.append(self.enque.pop())
        return self.enque[-1]
        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if len(self.deque)==0:
                return self.enque[-1]
            else:
                self.enque.append(self.deque.pop())
                
        return self.enque[-1]
