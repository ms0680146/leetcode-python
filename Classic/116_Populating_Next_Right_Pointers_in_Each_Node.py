'''
Given the above perfect binary tree. 
populate each next pointer to point to its next right node. 
'''

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root):
    if root and root.left and root.left:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        connect(root.left)
        connect(root.right)
    return root
