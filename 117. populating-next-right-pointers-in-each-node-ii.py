"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        from collections import deque
        if not root:
            return root
        q=deque()
        q.append(root)
        while q:
            tmp=[]
            for _ in range(len(q)):
                peek=q.popleft()
                tmp.append(peek)
                if peek.left:
                    q.append(peek.left)
                if peek.right:
                    q.append(peek.right)
            for i in range(len(tmp)):
                if i<len(tmp)-1:
                    tmp[i].next=tmp[i+1]
                else:
                    tmp[i].next=None
        return root