'''
Solution: Tree, Inorder
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Inorder: left -> node -> right
先走左邊並將node存進stack當中，當左邊都走完時，從stack pop出最上面的node，存進result當中，在開始走右邊。
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    stack = []
    result = []

    while root != None or len(stack) != 0:
        while root != None:
            stack.append(root)
            root = root.left
        
        root = stack.pop()
        result.append(root.val)
        root = root.right
    
    return result


'''  
Input: root = [1,null,2,3]
Output: [1,3,2]
'''