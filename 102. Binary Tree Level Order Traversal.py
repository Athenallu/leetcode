# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
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
            res.append(tmp)
        return res



        #if not root:
        #    return []
        #ans=[]
        #que=deque()
        #que.append(root)
        #count1=1
        #count2=0
        #while que:
        #    tmp=[]
        #    while count1:
        #        peek=que.popleft()
        #        tmp.append(peek.val)
        #        if peek.left:
        #            que.append(peek.left)
        #            count2+=1
        #        if peek.right:
        #            que.append(peek.right)
        #            count2+=1
        #        count1-=1
        #    ans.append(tmp)
        #    count1=count2
        #    count2=0
        #return ans


        #que.append([root])
        #while que:
        #    ans.append(que[0])
        #    lin=[]
        #    for item in que.popleft():
        #        if item.left:
        #            lin.append(item.left)
        #        if item.right:
        #            lin.append(item.right)
        #    que.append(lin)
        #return ans
            

