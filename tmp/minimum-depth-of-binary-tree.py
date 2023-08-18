
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def recur(cur):
            if not cur.left and not cur.right:
                return 1
            mini = float('inf')
            if cur.left:
                mini = min(mini, 1+recur(cur.left))
            if cur.right:
                mini = min(mini, 1+recur(cur.right))
            return mini
        return recur(root) if root else 0


            
        
