# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inlist=self.inorder(root)
        self.pos=-1

    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left)+[root.val]+self.inorder(root.right)

    def next(self) -> int:
        self.pos+=1
        return self.inlist[self.pos]
        
    def hasNext(self) -> bool:
        if self.pos<len(self.inlist)-1:
            return True
        else:
            return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()