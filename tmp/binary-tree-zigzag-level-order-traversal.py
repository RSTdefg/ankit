
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        if root:
            q.append(root)
        result = []
        flag = True
        while q:
            l = len(q)
            temp = []
            for _ in range(l):
                cur = q.popleft()
                temp.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if flag:
                result.append(temp)
            else:
                result.append(reversed(temp))
            flag = not flag
        return result


            


