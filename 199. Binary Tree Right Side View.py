# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[]
        from collections import deque
        q=deque()
        q.append(root)
        while q:
            tmp=[]
            for _ in range(len(q)):
                peek=q.popleft()
                tmp.append(peek.val)
                if peek.left:
                    q.append(peek.left)
                if peek.right:
                    q.append(peek.right)
            res.append(tmp[-1])
        return res


        #if not root:
        #    return []
        #ans=[]
        #que=deque()
        #que.append(root)
        #while que:
        #    tmp=[]
        #    for _ in range(len(que)):
        #        p=que.popleft()
        #        tmp.append(p.val)
        #        if p.left:
        #            que.append(p.left)
        #        if p.right:
        #            que.append(p.right)
        #    ans.append(tmp[-1])
        #return ans
