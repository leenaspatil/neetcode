from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: Optional[ListNode]) -> bool:

    slow = head
    fast = head

    while slow and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def main():
    nums = [100, 4, 200, 1, 3, 2]

    s = "leena"
    t = "neela"
    #  print(isAnagram(s, t))
    s, t = "anagram", "nagaram"
    # print(isAnagram(s, t))
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print((strs))


if __name__ == '__main__':
    main()
