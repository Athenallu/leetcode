# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self, root, path, res):
        path.append(str(root.val))
        if not root.left and not root.right:
            res.append(path[:])
            return
        if root.left:
            self.find(root.left, path, res)
            path.pop()
        if root.right:
            self.find(root.right, path, res)
            path.pop()

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res=[]
        self.find(root, [], res)
        ans=0
        for ele in res:
            ans+=int(''.join(ele))
        return ans

        

