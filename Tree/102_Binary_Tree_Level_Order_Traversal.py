'''
BFS (寬度優先搜尋)
1. BFS (寬度優先搜尋演算法): 是按照 '層' 的概念進行搜尋算法
2. 幾乎所有 BFS 題目都可以用 Queue 來記錄被展開的 TreeNode
3. Pseudo code
- Initialize Queue with tree root node.
- While Queue is not empty
  - for each node in the current queue
  - pull out the node
  - expand the node, push children to the Queue in order
  - increase level
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