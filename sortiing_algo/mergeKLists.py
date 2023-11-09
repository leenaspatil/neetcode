# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        val = val
        next = next


def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:  # [[1,4,5],[1,3,4],[2,6]]
        merge_list = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merge_list.append(self.mergeTwoLists(l1, l2))
        lists = merge_list

    return lists[0]

    def mergeTwoLists(self, list1, list2):
        if not list1:  # (not any value in list/stack....)
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)

        else:
            list2.next = self.mergeTwoLists(list1, list2.next)

        return list1 if list1.val < list2.val else list2


def main():
    list1 = ListNode[1]
    list1.next = ListNode[4]
    list1.next = ListNode[5]
    list2 = ListNode[1]
    list2.next = ListNode[4]
    list2.next = ListNode[5]
    lists = [list1,list2]
    mergeKLists(lists)


if __name__ == '__main__':
    main()
