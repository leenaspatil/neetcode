

class ListNode:
    def __init__(self, val, prev=None, next=None) -> None:
        self.val = val
        self.prev= prev
        self.next = next


class BrowserHistory:

    def __init__(self, homepage:str):
        self.curr = ListNode(homepage)

    def visit(self, url:str) -> None:
        self.curr.next = ListNode(url,self.curr)
        self.curr = self.curr.next

    def back(self, steps:int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1

