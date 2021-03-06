'''
BFS (寬度優先搜索)
依照層來進行搜尋
1. 創建一個 Queue，將 root node 寫進去
2. 檢查 queue 是否為空
3. 若不為空，表示還可以進行搜尋
4. for each queue, 並將 queue 的值 pop 出來
5. 去找此值的左右樹，並將其寫進 queue 當中
6. 增加 level
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def maxDepthBFS(root):
    queue = []
    level = 0
    
    if root is None:
        return level
    
    queue.append(root)
    while len(queue) > 0:
        for _ in range(len(queue)):    
            cur = queue.pop(0)
            if cur.left is not None:
                queue.append(cur.left)
            
            if cur.right is not None:
                queue.append(cur.right)
            
        level += 1
    return level

'''
DFS (深度優先搜索)
Buttom Up DFS
- Base Case
- 向子問題要答案(return value)
- 利用子問題的答案構建當前問題的答案
- 返回答案給父問題
'''
def maxDepthDFS(root):
    # Base Case
    if root is None: 
        return 0
    # 向左右子樹的子問題要答案
    leftLevel = maxDepthDFS(root.left)
    rightLevel = maxDepthDFS(root.right)
    # 利用子問題構建當前答案
    max_level = max(leftLevel, rightLevel) + 1
    # 返回答案給父問題
    return max_level