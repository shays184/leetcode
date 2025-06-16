from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root

        # if requested value equals node.val
        if node.val == val:
            return node     
        
        # if requested value is greater than node.val
        if node.val < val:
            if node.right is not None:
                return self.searchBST(node.right, val)
            else:
                return None
        
        # if requested value is less than node.val
        else:
            if node.left:
                return self.searchBST(node.left, val)
            else:
                return None

