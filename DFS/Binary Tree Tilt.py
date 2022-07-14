
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def tilt(node):
            if not node:
                return 0
            leftSum = tilt(node.left)
            rightSum = tilt(node.right)
            self.result += abs(leftSum - rightSum)
            return leftSum + rightSum + node.val
        tilt(root)
        return self.result
        
        