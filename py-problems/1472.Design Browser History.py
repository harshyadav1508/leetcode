# https://leetcode.com/problems/design-browser-history/description/

class ListNode:

    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.left=ListNode('left')
        self.right=ListNode('right')
        self.left.next=self.right
        self.right.prev=self.left
        prev,node, next=self.left,ListNode(homepage), self.right
        node.prev=prev
        node.next =next
        prev.next=node
        next.prev=node
        self.head=node
        
    def visit(self, url: str) -> None:

        prev,node, next=self.head,ListNode(url), self.right

        node.prev=prev
        node.next =next
        prev.next=node
        next.prev=node
        self.head=node

        
        

    def back(self, steps: int) -> str:
        cur=self.head
        while cur.prev!=self.left and steps:
            cur= cur.prev
            steps-=1
        if steps ==0 :
            self.head = cur
            return cur.val   
        if cur.prev==self.left:
            self.head=self.left.next
            return self.head.val
        
    def forward(self, steps: int) -> str:
        cur=self.head
        while cur.next!=self.right and steps:
            cur= cur.next
            steps-=1
        if steps ==0 :
            self.head =cur
            return cur.val   
        if  cur.next==self.right:
            self.head=self.right.prev
            return self.head.val


