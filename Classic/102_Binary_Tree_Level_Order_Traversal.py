'''
BFS (寬度優先搜尋)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def levelOrder(root):
    queue = []
    result = []
    
    if root == None:
        return result
    
    queue.append(root)

    while len(queue) > 0:
        level = []
        for _ in range(len(queue)):
            cur = queue.pop(0)
            level.append(cur.val)
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
        result.append(level)
        
    return result