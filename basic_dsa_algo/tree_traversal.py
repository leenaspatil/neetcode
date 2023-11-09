from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


#  For recursion, as discussed before, we need a base case and the function calling itself.


def searchBST_Iterative(root1: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    curr = root1

    while curr:
        if curr.val == val:
            print(curr.val)
            return curr
        elif val < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    return None


def searchBST_Recursive(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

    if root is None:
        return None

    if val > root.val:
        return searchBST_Recursive(root.right, val)
    elif val < root.val:
        return searchBST_Recursive(root.left, val)
    else:
        return root


def maxDepth(root: Optional[TreeNode]) -> int:

    if not root:
        print(root)
        return 0
    print(root.val)
    print("****")
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(0)
    root1.right.right = TreeNode(5)

    root = TreeNode(9)
    root.left = TreeNode(1)
    root.right = TreeNode(10)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(3)
    root.left.right.right = TreeNode(4)
    # Function call

    print(maxDepth(root))
  #  print(searchBST_Recursive(root1, 5))
   # print(searchBST_Recursive(root, 0))