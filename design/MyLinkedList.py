class ListNode:
    def __init__(self, x):
        self.val = x
        self.next, self.prev = None, None


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:

        if index < 0 or index >= self.size:
            return -1

        if index + 1 < self.size - index:  # (if index = 2 and size is 9 then  2 < 7)
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next

        else:  # (if index = 6 and size is 9 then  7 > 3)
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev

        return curr.val


    def addAtHead(self, val: int) -> None:
        pred, succ = self.head, self.head.next

        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add


    def addAtTail(self, val: int) -> None:
        pred, succ = self.tail, self.tail.prev

        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def addAtIndex(self, index: int, val: int) -> None:

        if index > self.size:
            return

        if index < 0:
            index = 0

        if index < self.size - index:

            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:

            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev

        self.size += 1
        node = ListNode(val)
        node.next = succ
        node.prev = pred
        succ.prev = node
        pred.next = node

    def deleteAtIndex(self, index: int) -> None:

        if index > self.size or  index > self.size:
            return

        if index < self.size - index:

            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:

            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev.prev

        self.size -= 1
        pred.next = succ
        succ.prev = pred

