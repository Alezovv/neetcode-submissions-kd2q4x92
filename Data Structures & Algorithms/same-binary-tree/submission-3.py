# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:

    def BFS(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        q1 = deque([p])
        q2 = deque([q])

        while q1 or q2:
            node1 = q1.popleft()
            node2 = q2.popleft()
            
            if (node1 is None) != (node2 is None):
                return False

            if node1 is None and node2 is None:
                continue

            if node1.val != node2.val:
                return False
            
            if node1.left is not None and node2.left is not None:
                q1.append(node1.left)
                q2.append(node2.left)
                ''' if self.BFS(q1, q2) == False:
                    return False '''
            elif node1.left is None and node2.left is None:
                pass
            else:
                return False

            if node1.right is not None and node2.right is not None:
                q1.append(node1.right)
                q2.append(node2.right)
                ''' if self.BFS(q1, q2) == False:
                    return False '''
            elif node1.right is None and node2.right is None:
                pass
            else:
                return False

        return True



    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        return self.BFS(p, q)



