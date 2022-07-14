# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import List
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root):
            queue = deque([root])
            answer = []
            while queue:
                visited = []
                size = len(queue)
                for i in range(size):
                    current = queue.popleft()
                    if current:
                        if current.left is not None:
                            queue.append(current.left)
                        if current.right is not None:
                            queue.append(current.right)
                    visited.append(current.val)
                answer.append(max(visited))
            return answer
        if root == None:
            return []
        return bfs(root)
        
        