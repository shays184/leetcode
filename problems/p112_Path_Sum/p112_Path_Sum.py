from typing import Optional
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        right_ans, left_ans = False, False

        if root is None: # if there is no node
            return False
        
        if (not root.right) and (not root.left): # leaf checking (A leaf is a node with no children.)
            if root.val == targetSum:
                return True
            return False
        
        if root.left: # checking the left root of a node
            left_ans = self.hasPathSum(root.left, targetSum-root.val)

        if root.right:  #if root.right is not NONE, checking the left root of a node
            right_ans = self.hasPathSum(root.right, targetSum-root.val)
        
        return right_ans or left_ans

#tree presentation example 
node1 = TreeNode(1)
node4_2 = TreeNode(4,right = node1) 
node2 = TreeNode(2)
node7 = TreeNode(7)
node13 = TreeNode(13)
node8 = TreeNode(8, left= node13,right= node4_2)
node11 = TreeNode(11, left=node7, right=node2)
node4_1 = TreeNode(4, left=node11)
node5 = TreeNode(5, left=node4_1, right=node8)


s= Solution()
s.hasPathSum(node5,22)
        


