# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, parent, grandparent):
            if node == None:
                return 0
            else:
                left_child = dfs(node.left, node, parent)
                right_child = dfs(node.right, node, parent)
                if grandparent != None and grandparent.val % 2 == 0:
                    return node.val + left_child + right_child
                return left_child + right_child
        return dfs(root, None, None)
