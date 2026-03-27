class linkedlist:
    def __init__(self, val, prev=None, next=None):
        self.val = val 
        self.next = next 
        self.prev = prev 


class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = linkedlist(homepage)

    def visit(self, url: str) -> None:
        new_node = linkedlist(url)
        self.curr.next = new_node
        new_node.prev = self.curr
        self.curr = new_node

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val