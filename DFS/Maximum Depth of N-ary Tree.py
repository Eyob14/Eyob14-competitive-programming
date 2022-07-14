"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from lib2to3.pytree import Node


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        maximum = 0
        for i in root.children:
            maximum = max(self.maxDepth(i), maximum)
        return maximum + 1
