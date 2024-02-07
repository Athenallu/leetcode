# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left)+[root.val]+self.inorder(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        inorder=self.inorder(root)
        for i in range(1,len(inorder)):
            if inorder[i]<=inorder[i-1]:
                return False
        return True
        #if inorder==sorted(inorder):
        #    return True
        #else:
        #    return False


    #    if not root:
    #        return True
    #    l=self.traversal(root)
    #    for i in range(1,len(l)):
    #        if l[i]<=l[i-1]:
    #            return False
    #    return True 
        
