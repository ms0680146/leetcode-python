'''
Solution: Tree, Dynamic Programming
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Input: numTrees(0), Output: 1
Input: numTrees(1), Output: 1
Input: numTrees(2) (use 1,2 as root), Output: numTrees(0)*numTrees(1) + numTrees(1)*numTrees(0)=2
Input: numTrees(3) (use 1,2,3 as root), Output: numTrees(0)*numTrees(2) + numTrees(1)*numTrees(1) + numTrees(2)*numTrees(0)
'''

def numTrees(n):
    numTree = {0:1, 1:1}
    for node in range(2, n+1): # n=2, range(2,3)=2
        total = 0
        for root in range(1, node+1): # node=2, range(1,3)=1,2
            left = numTree[root-1]
            right = numTree[node-root]
            total += left * right
        numTree[node] = total  
    
    return numTree[n]