'''
Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.

ex: 
    1
  2   3
N  5 N  N
Output: [[1,2,5], [1,3]]
Explanation: All root-to-leaf paths are: 1->2->5, 1->3

DFS:
把值透過參數的形式往下傳遞
top down dfs 一般來說不返回值
- Base Case
- 利用父問題傳下來的值做計算
- 把值傳給子問題做 recursion
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def binaryTreePaths(root):
    result = []
    
    if root is None:
        return result
    
    dfs(result, root, [])
    return result

def dfs(result, root, path): 
    # Base Case
    if root is None:
        return

    # 把父問題傳下來的值做計算
    # copy 一份避免影響到原本的 path
    path_copy = path.copy()
    path_copy.append(root.val) 
    
    if root.left is None and root.right is None:
        result.append(path_copy)
        return

    # 把值傳給子問題做 recursion
    dfs(result, root.left, path_copy)
    dfs(result, root.right, path_copy)
        
    