
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def inverse(root):
            if not root:
                return root
            l = inverse(root.left)
            r = inverse(root.right)
            root.left, root.right = r, l
            return root
        def same(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2 or t1.val != t2.val:
                return False
            return same(t1.left, t2.left) and same(t1.right, t2.right)
        return same(inverse(root.left), root.right)
            
