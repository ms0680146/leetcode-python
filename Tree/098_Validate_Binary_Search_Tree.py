'''
Solution: Tree, Recursion
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:

1. The left subtree of a node contains only nodes with keys less than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.

檢查每個node是否介於臨界值之間。
root -> float('-inf') ~ float('inf')
left -> float('-inf') ~ root.val
right -> root.val ~ float('inf')
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    return helper(root, float('-inf'), float('inf'))


def helper(root, min, max):
    if root == None:
        return True

    if root.val >= max or root.val <= min:
        return False

    return helper(root.left, min, root.val) and helper(root.right, root.val, max)
