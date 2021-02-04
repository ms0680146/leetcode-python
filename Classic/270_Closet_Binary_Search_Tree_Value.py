'''
Find the closest value in Binary Search Tree
input: BST
output: node data

current_diff, min_diff, min_diff_node
'''

class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def findClosestValueInBST(node, value):
    if not node:
        return None

    min_diff = float('inf')
    min_diff_node = None

    while node != None:
        current_diff = abs(node.value - value)
        if current_diff < min_diff:
            min_diff = current_diff
            min_diff_node = node

        if value < node.value:
            node = node.left
        elif value > node.value:
            node = node.right
        else:
            break

    return min_diff_node
