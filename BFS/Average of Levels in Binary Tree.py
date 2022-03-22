# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import statistics as s
class Solution:
    def average(self, arr):
        total = sum(arr)
        return total/len(arr)
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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
                answer.append(self.average(visited))
            return answer
        return bfs(root)
        