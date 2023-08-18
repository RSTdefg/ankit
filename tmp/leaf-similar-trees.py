
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        result = []
        def recur(root):
            if not root:
                return
            if not root.right and not root.left:
                result.append(root.val)
                return
            recur(root.left)
            recur(root.right)
            return
        recur(root1)
        recur(root2)
        return result[:len(result)//2] == result[len(result)//2:]

