from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insertIntoBST(self,root.left,val)
    else:
        root.right = insertIntoBST(self,root.right,val)
    return root