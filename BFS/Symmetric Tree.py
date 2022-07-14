# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def palindrom(self, arr):
        if arr == arr[::-1]:
            return True
        return False
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def bfs(root):
            queue = deque([root])
            answer = True
            while queue:
                visited = []
                size = len(queue)
                for i in range(size):
                    current = queue.popleft()
                    if current:
                        queue.append(current.left)
                        queue.append(current.right)
                    if current:
                        visited.append(current.val)
                    else:
                        visited.append(None)
                if not(self.palindrom(visited)):
                    answer = False
            return answer
        return bfs(root)