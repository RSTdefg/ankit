
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            last = None
            for _ in range(size):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                last = cur.val
            res.append(last)
        return res


