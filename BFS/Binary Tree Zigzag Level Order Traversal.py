# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            queue = deque([root])
            answer = []
            direction = 0
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
                direction += 1
                if direction % 2 != 0:
                    answer.append(visited)
                else:
                    answer.append(visited[::-1])
            return answer
        if not(root):
            return []
        return bfs(root)